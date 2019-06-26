
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.graph_objs as go
from bs4 import BeautifulSoup
import requests
def users(name1,name2):
    temp = requests.get('https://twitter.com/'+name1)
    bs = BeautifulSoup(temp.text,'lxml')
    try:
    #    follow_box = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--followers'})
    #    followers = follow_box.find('a').find('span',{'class':'ProfileNav-value'})
        all_tabs = bs.find_all("li",class_="ProfileNav-item")
        
        feature_dict = {}
        feature_req = ["Followers","Following","Tweets"]
        feature_dict = feature_dict.fromkeys(feature_req,0)
        
        
        for item in all_tabs:
            label = item.find("span",class_="ProfileNav-label")
            value = item.find("span",class_="ProfileNav-value")
            
            if label and value:
                label = str(label.text.strip())
                value = str(value.text.strip())
                if label in feature_req:
                    feature_dict[label] = value
        
        xx=feature_dict
        import re
        #extracting the image of user1
        pic=bs.find_all("img",{"class": "ProfileAvatar-image "})
        if(len(pic) != 0):
            url1=pic[0]['src']
        else:
            url1="http://rollacosta.in/wp-content/uploads/2017/04/dummy-pic.png"
            
        
    except:
        print('Account name not found...')
        
     
    temp = requests.get('https://twitter.com/'+name2)
    bs = BeautifulSoup(temp.text,'lxml')
    try:
    #    follow_box = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--followers'})
    #    followers = follow_box.find('a').find('span',{'class':'ProfileNav-value'})
        all_tabs = bs.find_all("li",class_="ProfileNav-item")
        
        feature_dict1 = {}
        
        feature_dict1 = feature_dict1.fromkeys(feature_req,0)
        
        for item in all_tabs:
            label = item.find("span",class_="ProfileNav-label")
            value = item.find("span",class_="ProfileNav-value")
            
            if label and value:
                label = str(label.text.strip())
                value = str(value.text.strip())
                if label in feature_req:
                    feature_dict1[label] = value
        yy=feature_dict1
        #extracting image of user2
        pic=bs.find_all("img",{"class": "ProfileAvatar-image "})
        if(len(pic) != 0):
            url2=pic[0]['src']
        else:
            url2="http://rollacosta.in/wp-content/uploads/2017/04/dummy-pic.png"
    except:
        print('Account name not found...')
       
    for key,value in feature_dict.items():
        
        if(re.search(r'[,]',str(value))):
            value=value.replace(",","")
            
             
     
                
        if(re.search(r'M$',str(value))):
            value=float(value.replace("M",""))
            value=int(value*1000000)
        
        elif(re.search(r'K$',str(value))):
            value=float(value.replace("K",""))
            value=int(value*1000)
        feature_dict[key]=int(value)
                
    for key,value in feature_dict1.items():
        if(re.search(r'[,]',str(value))):
            value=value.replace(",","")
                         
        if(re.search(r'M$',str(value))):
            value=float(value.replace("M",""))
            value=int(value*1000000)
        
        if(re.search(r'K$',str(value))):
            value=float(value.replace("K",""))
            value=int(value*1000)
        feature_dict1[key]=int(value)
    
            
        
    
    list1=[feature_dict["Followers"],feature_dict["Following"],feature_dict["Tweets"],feature_dict1["Followers"],feature_dict1["Following"],feature_dict1["Tweets"]]
    
    import pickle
    with open("pick_pickle",'rb') as fp:
        classifier=pickle.load(fp)    
    
    
    with open("pick_pickle1",'rb') as fp1:
        sc=pickle.load(fp1)

        
    import numpy as np
    list2=np.array(list1)
    list2=list2.reshape(1,-1)
    
    list2=sc.transform(list2)
    
    
    x=classifier.predict(list2)
    
    #plotting the bar graph in which we compare the different features of both user
    trace1 = go.Bar(
    x=[name1,name2],
    y=[feature_dict["Followers"],feature_dict1["Followers"]],
    name='Followers'
    )
    trace2 = go.Bar(
    x=[name1,name2],
    y=[feature_dict["Following"],feature_dict1["Following"]],
    name='Following'
    )
    trace3 = go.Bar(
    x=[name1,name2],
    y=[feature_dict["Tweets"],feature_dict1["Tweets"]],
    name='Tweets'
    )
    data = [trace1, trace2,trace3]
    updatemenus = list([
        dict(type="buttons",
             active=-1,
             buttons=list([
                dict(label = 'Followers',
                     method = 'update',
                     args = [{'visible': [True, True, False]},
                             {'title': 'Followers'}]),
                dict(label = 'Following',
                     method = 'update',
                     args = [{'visible': [False,True, False]},
                             {'title': 'Following'}]),
                dict(label = 'Tweets',
                     method = 'update',
                     args = [{'visible': [False,False,True]},
                             {'title': 'Tweets'}]),
                dict(label = 'All',
                     method = 'update',
                     args = [{'visible': [True, True, True]},
                             {'title': 'Features'}])
            ]),
        )
    ])
    
    layout = go.Layout(barmode='group', updatemenus=updatemenus)

    fig = go.Figure(data=data, layout=layout)
    figs=plot(fig, filename='grouped-bar',output_type='div')
    
    
    fig = {
    'data': [
    {
    'labels': [name1,name2],
    'values': [feature_dict["Followers"],feature_dict1["Followers"]],
    'type': 'pie',
    'name': 'Followers',
    'marker': {'colors': ['rgb(0, 75, 166)',
      'rgb(255, 95, 29)']},
    'domain': {'x': [0, .48],
       'y': [0, .49]},
    'hoverinfo':'all',
    'textinfo':'label'
    },
    {
    'labels': [name1,name2],
    'values': [feature_dict["Following"],feature_dict1["Following"]],
    'marker': {'colors': ['rgb(0, 75, 166)',
      'rgb(255, 95, 29)']},
    'type': 'pie',
    'name': 'Following',
    'domain': {'x': [.52, 1],
       'y': [0, .49]},
    'hoverinfo':'all',
    'textinfo':'label'
    
    },
    {
    'labels': [name1,name2],
    'values': [feature_dict["Tweets"],feature_dict1["Tweets"]],
    'marker': {'colors': ['rgb(0, 75, 166)',
      'rgb(255, 95, 29)']},
    'type': 'pie',
    'name': 'Tweets',
    'domain': {'x': [0, .48],
       'y': [.51, 1]},
    'hoverinfo':'all',
    'textinfo':'label'
    }],
    'layout': {'title': 'Features analyse',
       'showlegend': True}
    }
    fig1=plot(fig, filename='pie_chart_subplots',output_type='div')



    if x==1:
        return (xx,yy,name1,url1,url2,figs,fig1)
    else:
        return (xx,yy,name2,url1,url2,figs,fig1)