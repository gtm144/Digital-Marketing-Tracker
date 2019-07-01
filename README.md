# Digital-Marketing-Tracker
A google sheets automize tracker that collected data from Appnexus and Doubleclick marketing campaigns.

Back in the days when I worked as digital marketing trader, I have to update metrics from advertising campaigns everyday manually from many programmatic demand-side platforms, such as Appnexus and Doubleclick manager, on a googlesheet. This process was eventually tedious so I automitize a way that on 2 a.m., python modules would do this job for me to let me concentrate in other aspects of my work.

**en.py:** Module connects directly to googlesheets to write and modify cells accordingly to params such as kpi, DSP, impressions the advertising campaign was needed.

**rep_an.py:** Module which extracts data from Appnexus to pass it down to en.py by its call.

**rep_dbm.py:** Module which extracts data from DoubleClick Manager to pass it down to en.py by its call.
