pacman::p_load("pdftools","stringr",data.table,magrittr,dplyr,RColorBrewer,tm,
               wordcloud2,lubridate,SnowballC,ggplot2,highcharter,openxlsx,webshot,htmlwidgets,wordcloud)

setwd("D:/users/deyanlin/desktop/eda_viz/MPC/")
files = list.files("D:/users/deyanlin/desktop/eda_viz/MPC/",all.files = T,pattern = "*.pdf")

dt = data.table()

for(i in 1:length(files)){
  temp = paste(pdf_text(files[i]),collapse = "") %>% as.data.table()
  filename = str_remove(files[i],pattern = ".pdf")
  print(filename)
  temp$date = filename
  dt = rbind(dt,temp)
}

dt %>% setnames(.,c("text","date")) %>% 
  .[,MonthYear:=str_replace(date,"MPC_","")] %>% .[,MonthYear:=as.Date(MonthYear,format="%d%B%Y")]
dt %>%
  .[,text:=lapply(text,function(x){ sub('.*At its meeting today', 'At its meeting today', x)})]%>%
  .[,text:=lapply(text,function(x){ sub('\\s+Bank Negara Malaysia\\r\n\\     [0-9].*', '', x)})]%>%
  .[,text:=lapply(text,function(x){ sub('.*At the Monetary Policy Committee', 'At the Monetary Policy Committee', x)})] %>%
  .[,text:=lapply(text,function(x){ sub('.*At its Monetary Policy Committee', 'At its Monetary Policy Committee', x)})]%>%
  .[,text:=tolower(text)]%>%
  .[,text:=lapply(text,function(x){ gsub('\\s+the\\s+', '', x)})]%>%
  .[,text:=lapply(text,function(x){ gsub('mpc', '', x)})] %>%
  .[,text:=lapply(text,function(x){ gsub('bank negara malaysia\\b', '', x)})] %>%
  .[,text:=lapply(text,function(x){ gsub('monetary policy committee', '', x)})]%>%
  .[,text:=lapply(text,function(x){ gsub('will', '', x)})]%>%
  .[,text:=lapply(text,function(x){ gsub('today', '', x)})]%>%
  .[,text:=lapply(text,function(x){ gsub('however', '', x)})]

#before ge14----
dtbeforemay18 = dt[MonthYear<="2018-05-09"]
test = dtbeforemay18$text %>% unlist %>% paste(collapse = "")
docs = Corpus(VectorSource(test)) %>%
  tm_map(removeNumbers)%>%
  tm_map(removePunctuation)%>%
  tm_map(stripWhitespace) %>%
  tm_map(removeWords,stopwords("english"))

dtm <- TermDocumentMatrix(docs) 
matrix <- as.matrix(dtm) 
words <- sort(rowSums(matrix),decreasing=TRUE) 
df <- data.frame(word = names(words),freq=words) %>% as.data.table()

#generate word cloud
wordcloud(words = df$word, freq = df$freq, min.freq = 10,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))

#afterge14----
dtaftermay18 = dt[MonthYear>"2018-05-09"]
test1 = dtaftermay18$text %>% unlist %>% paste(collapse = "")
docs1 = Corpus(VectorSource(test1)) %>%
  tm_map(removeNumbers)%>%
  tm_map(removePunctuation)%>%
  tm_map(stripWhitespace) %>%
  tm_map(removeWords,stopwords("english"))

dtm1 <- TermDocumentMatrix(docs1) 
matrix1 <- as.matrix(dtm1) 
words1 <- sort(rowSums(matrix1),decreasing=TRUE) 
df1 <- data.frame(word = names(words1),freq=words1)%>% as.data.table()

#generate word cloud
wordcloud2(data=df1, size = 0.7, shape = 'pentagon')

#generate top10 words
top10words = cbind(df[1:10],df1[1:10])%>% setnames(c("Word_Before","Freq_Before","Word_After","Freq_After")) 

#visualize MPC sentiment result----
filename1 = "D:/users/deyanlin/desktop/eda_viz/MPC/2020-11-21_MPCfinalResult.xlsx"
dt = read.xlsx(filename1,detectDates = T) %>% as.data.table%>%.[order(`MPCDate`)] %>% .[,MPCDate:=format(MPCDate,"%b %Y")]
highchart()%>%
  hc_xAxis(categories = unique(dt$MPCDate)) %>%
  hc_add_series(name="Sentiment",data=dt$SentimentScore,color="#00203FFF")%>%
  hc_xAxis(
    plotBands = list(
      list(
        label = list(text = "Post GE14"),
        color = "#C7F9EE",
        from = 11,
        to = 23
      )
    )
  )%>%
  hc_yAxis(
    title = list(text = "Net Sentiment Score", useHTML = TRUE)
  ) %>%
  hc_xAxis(title = list(text = "Year", useHTML = TRUE),labels = list(format = '{value:%B %Y}'))