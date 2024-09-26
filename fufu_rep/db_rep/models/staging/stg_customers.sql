{{ config(materialized='table') }}

select
    customer_id as id,
    first_name,
    last_name,
    gender,
    loyalty_status
from {{ ref('stg_customers') }}