

select *
from {{ ref('my_second_dbt_model') }}
union all
select 2