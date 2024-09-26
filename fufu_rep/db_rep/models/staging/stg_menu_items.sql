{{ config(materialized='table') }}

select
    transaction_id,
    customer_id,
    item_id,
    amount,
    transaction_date
from {{ ref('stg_transactions') }}