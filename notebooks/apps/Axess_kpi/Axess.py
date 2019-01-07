# Databricks notebook source
from PassageFiltered import PassageFiltered
from WorkingTable import WorkingTable
from KPI import KPI

# COMMAND ----------

passage_filter = PassageFiltered(
  spark, 
  dbutils.widgets.get("ClientId"),
  #dbutils.widgets.get("ProcessDate"),
)
passage_filter.run()

# COMMAND ----------

working_table = WorkingTable.from_PassageFiltered(passage_filter)
working_table.run()

# COMMAND ----------

kpi = KPI.from_WorkingTable(working_table)
kpi.run()

# COMMAND ----------

