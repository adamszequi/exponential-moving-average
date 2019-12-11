# exponential-moving-average

The EMA is similar to the simple moving average, but, instead of weighing all prices in the
history equally, it places more weight on the most recent price observation and less weight
on the older price observations. This is endeavoring to capture the intuitive idea that the
new price observation has more up-to-date information than prices in the past. It is also
possible to place more weight on older price observations and less weight on the newer
price observations. This would try to capture the idea that longer-term trends have more
information than short-term volatile price movements.

The weighting depends on the selected time period of the EMA; the shorter the time period,
the more reactive the EMA is to new price observations; in other words, the EMA
converges to new price observations faster and forgets older observations faster, also
referred to as Fast EMA. The longer the time period, the less reactive the EMA is to new
price observations; that is, EMA converges to new price observations slower and forgets
older observations slower, also referred to as Slow EMA.
Based on the description of EMA, it is formulated as a weight factor, , applied to new price
observations and a weight factor applied to the current value of EMA to get the new value
of EMA.
