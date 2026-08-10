-- ==============================================================================
-- 🔍 CAPA VECTORIAL: BÚSQUEDA POR SIMILITUD (Supabase pgvector / Vector Store)
-- ==============================================================================
-- Firma de diseño: SQL / Vector Store / HNSW / IVF FLAT
-- Propósito: Buscar información no estructurada por "sentido semántico".
-- Regla de Oro: Ideal para FAQs, políticas, manuales y RAG no estructurado.
-- ==============================================================================

-- 1. Habilitar la extensión de vectores en PostgreSQL (pgvector)
CREATE EXTENSION IF NOT EXISTS vector;

-- 2. Tabla de Base de Conocimientos (Knowledge Base)
CREATE TABLE IF NOT EXISTS public.documentos_kb (
    id BIGSERIAL PRIMARY KEY,
    titulo TEXT NOT NULL,
    contenido TEXT NOT NULL,
    categoria_semantica TEXT NOT NULL CHECK (categoria_semantica IN ('soporte', 'politicas', 'manuales', 'faq')),
    pregunta_hipotetica TEXT,
    metadata JSONB DEFAULT '{}'::jsonb,
    embedding VECTOR(1536), -- Vector denso (ej. text-embedding-3-small de OpenAI)
    creado_en TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Comentarios explicativos de la capa vectorial
COMMENT ON TABLE public.documentos_kb IS 'Capa Vectorial: Almacén de fragmentos de texto con embeddings para RAG.';
COMMENT ON COLUMN public.documentos_kb.embedding IS 'Vector de 1536 dimensiones para búsqueda por similitud de coseno.';

-- 3. Índice HNSW para búsquedas vectoriales ultra rápidas
CREATE INDEX IF NOT EXISTS idx_documentos_kb_embedding_hnsw 
ON public.documentos_kb 
USING hnsw (embedding vector_cosine_ops);

-- 4. Función de RPC para buscar documentos similares en Supabase / Postgres
CREATE OR REPLACE FUNCTION buscar_documentos_similares (
  query_embedding VECTOR(1536),
  match_threshold FLOAT,
  match_count INT
)
RETURNS TABLE (
  id BIGINT,
  titulo TEXT,
  contenido TEXT,
  categoria_semantica TEXT,
  similarity FLOAT
)
LANGUAGE sql STABLE
AS $$
  SELECT
    public.documentos_kb.id,
    public.documentos_kb.titulo,
    public.documentos_kb.contenido,
    public.documentos_kb.categoria_semantica,
    1 - (public.documentos_kb.embedding <=> query_embedding) AS similarity
  FROM public.documentos_kb
  WHERE 1 - (public.documentos_kb.embedding <=> query_embedding) > match_threshold
  ORDER BY public.documentos_kb.embedding <=> query_embedding
  LIMIT match_count;
$$;
