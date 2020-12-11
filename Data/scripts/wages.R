pacman::p_load(data.table,magrittr,openxlsx,ggplot2,gridExtra)

filename1 = "D:/users/deyanlin/desktop/eda_viz/Wages_Stats.xlsx"
sheetnames = getSheetNames(filename1)

#compare by age----
dt_age = read.xlsx(xlsxFile = filename1,sheet = 1) %>% as.data.table() %>%
  .[15:26]%>% .[,-c(12)]
colnames=c("Age",seq(from=2010,to = 2019))
dt_age1 = dt_age%>%setnames(colnames) %>% .[2:nrow(.)] %>% .[,c("Age","2016","2017","2018","2019")]
dt_age_long = melt(dt_age1,id.var="Age") %>% .[Age!="Jumlah"]  
dt_age_increment = dt_age%>%setnames(colnames) %>% .[2:nrow(.)] %>% .[,c("Age","2015","2016","2017","2018","2019")]%>%
  .[,Increment_2016:=round((`2016`-`2015`)/`2015`*100,digits = 2),by=Age]%>%
  .[,Increment_2017:=round((`2017`-`2016`)/`2016`*100,digits = 2),by=Age]%>%
  .[,Increment_2018:=round((`2018`-`2017`)/`2017`*100,digits = 2),by=Age]%>%
  .[,Increment_2019:=round((`2019`-`2018`)/`2018`*100,digits = 2),by=Age] %>%
  .[,-c(2:6)] %>% setnames(c("Age","2016","2017","2018","2019"))
dt_age_increment_long = melt(dt_age_increment,id.var="Age")

#plot for wage increment for 15-29
highchart() %>% 
  hc_xAxis(categories = unique(dt_age_increment_long$variable))%>% 
  hc_add_series(
    name = "15-19", data = dt_age_increment_long[Age=="15-19"]$value, lineWidth=3, color="#21313E"
  ) %>% 
  hc_add_series(
    name = "20-24", data = dt_age_increment_long[Age=="20-24"]$value, lineWidth=3, color="#268073"
  ) %>% 
  hc_add_series(
    name = "25-29", data = dt_age_increment_long[Age=="25-29"]$value, lineWidth=3, color="#98CF6F"
  ) %>%
  hc_add_series(
    name = "Average", data = dt_age_increment_long[Age=="Jumlah"]$value, color="#e74c3c"
  ) %>%
  hc_yAxis(
    title = list(text = "Increment (%)", useHTML = TRUE)
  ) %>%
  hc_xAxis(
    title = list(text = "Year")
  )%>% 
  hc_title(
    text = "Average Wage Increment for Employees Aged between 15 to 29 Relative to National Average"
  )

#plot for wage increment for 30-59
highchart() %>% 
  hc_xAxis(categories = unique(dt_age_increment_long$variable))%>% 
  hc_add_series(
    name = "30-34", data = dt_age_increment_long[Age=="30-34"]$value, lineWidth=3, color="#10252D"
  ) %>% 
  hc_add_series(
    name = "35-39", data = dt_age_increment_long[Age=="35-39"]$value, lineWidth=3, color="#20434E"
  ) %>% 
  hc_add_series(
    name = "40-44", data = dt_age_increment_long[Age=="40-44"]$value, lineWidth=3, color="#316373"
  ) %>%
  hc_add_series(
    name = "45-49", data = dt_age_increment_long[Age=="45-49"]$value, lineWidth=3, color="#428599"
  ) %>%
  hc_add_series(
    name = "50-54", data = dt_age_increment_long[Age=="50-54"]$value, lineWidth=3, color="#53A8C0"
  ) %>%
  hc_add_series(
    name = "Average", data = dt_age_increment_long[Age=="Jumlah"]$value, color="#e74c3c"
  ) %>%
  hc_yAxis(
    title = list(text = "Increment (%)", useHTML = TRUE)
  ) %>%
  hc_xAxis(
    title = list(text = "Year")
  )%>% 
  hc_title(
    text = "Average Wage Increment for Employees Aged between 30 to 54 Relative to National Average"
  )

#compare by urban rural +state----
dt_urbanrural = read.xlsx(xlsxFile = filename1,sheet = 8) %>% as.data.table() %>% .[8:9,] %>% .[,-c(12)]
colnames1 = c("Strata",seq(from=2010,to = 2019))
dt_urbanrural1 = dt_urbanrural %>% setnames(colnames1) %>% .[,-c(2:7)]
dt_urbanrural_long = melt(dt_urbanrural1,id.vars = "Strata")
dt_urbanrural2 = dt_urbanrural%>%setnames(colnames1) %>% .[,c("Strata","2015","2016","2017","2018","2019")]%>%
  .[,Increment_2016:=round((`2016`-`2015`)/`2015`*100,digits = 2),by=Strata]%>%
  .[,Increment_2017:=round((`2017`-`2016`)/`2016`*100,digits = 2),by=Strata]%>%
  .[,Increment_2018:=round((`2018`-`2017`)/`2017`*100,digits = 2),by=Strata]%>%
  .[,Increment_2019:=round((`2019`-`2018`)/`2018`*100,digits = 2),by=Strata]%>%
  .[,-c(2:6)] %>% setnames(c("Strata","2016","2017","2018","2019"))
dt_urbrul_increment_long = melt(dt_urbanrural2,id.var="Strata")

highchart() %>% 
  hc_xAxis(categories = unique(dt_urbrul_increment_long$variable))%>% 
  hc_add_series(
    name = "Urban", data = dt_urbrul_increment_long[Strata=="Bandar"]$value, lineWidth=3
  ) %>% 
  hc_add_series(
    name = "Rural", data = dt_urbrul_increment_long[Strata=="Luar Bandar"]$value, lineWidth=3
  )%>%
  hc_yAxis(
    title = list(text = "Increment (%)", useHTML = TRUE)
  ) %>%
  hc_xAxis(
    title = list(text = "Year")
  )%>% 
  hc_title(
    text = "Average Wage Increment of Urban and Rural Employees"
  )

