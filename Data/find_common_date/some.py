select f1.*
from my_features f1
where exists (select 1
              from my_features f2
              where tsrange(f2.begin_time, f2.end_time, '[]') && tsrange(f1.begin_time, f1.end_time, '[]')
                and f2.feature_id = f1.feature_id
                and f2.id <> f1.id);