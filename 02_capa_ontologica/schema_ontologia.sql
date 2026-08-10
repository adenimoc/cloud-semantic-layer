-- ==============================================================================
-- 🌐 CAPA ONTOLÓGICA: ENTIDADES Y JERARQUÍAS (PostgreSQL / Relacional / Grafos)
-- ==============================================================================
-- Firma de diseño: JSON / SQL / Grafos (Neo4j, Cypher, SQL DDL)
-- Propósito: Definir la taxonomía del negocio, pertenencias y relaciones unívocas.
-- Regla de Oro: Las relaciones ("X es filial de Y") son HECHOS ESTÁTICOS, no adivinanzas.
-- ==============================================================================

-- 1. Entidad Matriz: Organizaciones
CREATE TABLE IF NOT EXISTS public.organizaciones (
    id BIGSERIAL PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE,
    codigo_taxonomico TEXT NOT NULL UNIQUE,
    pais_origen VARCHAR(3) NOT NULL,
    creado_en TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Metadatos ontológicos explicativos para el motor semántico/LLM
COMMENT ON TABLE public.organizaciones IS 'Ontología: Entidad Matriz Corporativa. Define la cima de la jerarquía de clientes.';
COMMENT ON COLUMN public.organizaciones.codigo_taxonomico IS 'Clave taxonómica única para mapear estructuras organizacionales externas.';

-- 2. Entidad Dependiente: Clientes
CREATE TABLE IF NOT EXISTS public.clientes (
    id BIGSERIAL PRIMARY KEY,
    organizacion_id BIGINT NOT NULL REFERENCES public.organizaciones(id) ON DELETE RESTRICT,
    nombre_contacto TEXT NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    tipo_cliente TEXT NOT NULL CHECK (tipo_cliente IN ('enterprise', 'pyme', 'individual')),
    estado_cuenta TEXT NOT NULL DEFAULT 'activo' CHECK (estado_cuenta IN ('activo', 'suspendido', 'inactivo')),
    creado_en TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE public.clientes IS 'Ontología: Entidad consumidora. Pertenece a una Organización matriz obligatoriamente.';
COMMENT ON COLUMN public.clientes.organizacion_id IS 'Relación de pertenencia directa (FK a public.organizaciones).';

-- 3. Entidad de Dominio: Transacciones de Venta
CREATE TABLE IF NOT EXISTS public.ventas (
    id BIGSERIAL PRIMARY KEY,
    cliente_id BIGINT NOT NULL REFERENCES public.clientes(id) ON DELETE RESTRICT,
    monto NUMERIC(12, 2) NOT NULL CHECK (monto >= 0),
    descuento NUMERIC(12, 2) NOT NULL DEFAULT 0.00 CHECK (descuento >= 0),
    estado TEXT NOT NULL DEFAULT 'completada' CHECK (estado IN ('completada', 'pendiente', 'cancelada')),
    metodo_pago TEXT NOT NULL CHECK (metodo_pago IN ('tarjeta_credito', 'transferencia', 'paypal')),
    fecha_creacion TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE public.ventas IS 'Ontología: Registro de evento transaccional. Vincula a un Cliente específico.';
