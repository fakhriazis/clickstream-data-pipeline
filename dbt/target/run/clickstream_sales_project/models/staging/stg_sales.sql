
  create view "airflow"."public"."stg_sales__dbt_tmp"
    
    
  as (
    -- staging model: clean and rename raw sales data
with source as (
  select * from "airflow"."public"."sales_staging"
),

renamed as (
  select
    order_id,
    product_id,
    customer_id,
    quantity,
    total_price,
    order_date
  from source
)

select * from renamed
  );