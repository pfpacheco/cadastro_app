create table tb_cadastro(
    uuid uuid primary key default gen_random_uuid(),
    name text not null,
    cnu char(20) not null,
    description text not null,
    created_at timestamp not null default now(),
    updated_at timestamp default null,
    unique (cnu)
);