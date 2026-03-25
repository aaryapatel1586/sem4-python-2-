#!/usr/bin/env python
# coding: utf-8

# ## Heatmaps

# - seaborn.heatmap(data,vmin=None,vmax=None,linewidths=0,linecolor='white',annot=True,)

# In[1]:


# importing the modules
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data=np.random.randint(low=1,high=100,size=(10,10))
print("The data to be plotted:\n")
print(data)
sns.heatmap(data)
plt.show()


# In[2]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data=np.random.randint(low=1,high=100,size=(10,10))
print("The data to be plotted:\n")
print(data)
sns.heatmap(data,annot=True)
plt.show()


# In[3]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data=np.random.randint(low=1,high=100,size=(10,10))
print("The data to be plotted:\n")
print(data)
sns.heatmap(data,vmin=30,vmax=70)
plt.show()


# In[4]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data=np.random.randint(low=1,high=100,size=(10,10))
print("The data to be plotted:\n")
print(data)
sns.heatmap(data,vmin=30,vmax=70,annot=True)
plt.show()


# In[5]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data=np.random.randint(low=1,high=100,size=(10,10))
print("The data to be plotted:\n")
print(data)
sns.heatmap(data,cmap="tab20")
plt.show()


# In[9]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data=np.random.randint(low=1,high=100,size=(10,10))
print("The data to be plotted:\n")
print(data)
hm=sns.heatmap(data,vmin=10,vmax=70,cmap='Pastel1',annot=True,linewidths=1,linecolor='black',cbar=False,xticklabels=False,
           yticklabels=False)
plt.show()


# In[10]:


import numpy as np
import pandas as pd
df=pd.DataFrame(np.random.random((5,5)),columns=["a","b","c","d","e"])
print(df)
p1=sns.heatmap(df)


# In[14]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data=np.random.randint(low=1,high=100,size=(3,10))
print("The data to be plotted:\n")
print(data)
plt.figure(figsize=(15,5))
hm=sns.heatmap(data,vmin=10,vmax=70,cmap='Pastel1',annot=True,linewidths=2,linecolor='black',cbar=True,xticklabels=True,
           yticklabels=True)
plt.show()


# In[15]:


import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('auto-mpg.csv')
sns.boxplot(y=df['mpg'])
plt.show()


# In[16]:


import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('auto-mpg.csv')
sns.boxplot(y=df['acceleration'])
plt.show()


# In[18]:


import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('auto-mpg.csv')
sns.boxplot(x=df['acceleration'],data=df)
plt.show()


# In[20]:


import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset("tips")
sns.boxplot(x="day",y="total_bill",hue="smoker",data=df)
plt.show()


# In[22]:


import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset("tips")
sns.boxplot(x="day",y="tip",data=df)
plt.show()


# ## Scatterplot

# In[23]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('auto-mpg.csv')

df['horsepower']=pd.to_numeric(df['horsepower'],errors='coerce')
df=df.dropna(subset=['horsepower'])
plt.figure(figsize=(10,6))

sns.scatterplot(data=df,
                x='horsepower',   #horizontal axis
                y='mpg',hue='origin',
                style='origin',
                size='weight',
                palette='Set1')
plt.title("MPG ")
plt.tight_layout()
plt.show()


# In[24]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('auto-mpg.csv')

df['horsepower']=pd.to_numeric(df['horsepower'],errors='coerce')
df=df.dropna(subset=['horsepower'])
plt.figure(figsize=(10,6))

sns.scatterplot(data=df,
                x='horsepower',   #horizontal axis
                y='mpg')
plt.title("MPG ")
plt.tight_layout()
plt.show()


# In[ ]:


#25/3/2026


# ## Visualizing Graphs usig NetworkX Library

# ### Undirected Graphs

# In[3]:


import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from(range(4,7))

G.add_edge(1,2)
G.add_edge(1,1)
G.add_edges_from([(2,3),(3,6),(4,6),(5,6)])

nx.draw_networkx(G,node_size=850,node_color='red',width=2,edge_color='blue')
plt.show()


# ### Directed Graph

# In[6]:


import networkx as nx
import matplotlib.pyplot as plt

g=nx.DiGraph()
g.add_nodes_from([1,2,3,4,5])

g.add_edge(1,2)
g.add_edge(4,2)
g.add_edge(3,5)
g.add_edge(2,3)
g.add_edge(5,4)

nx.draw(g,with_labels=True,node_size=1000,node_color='red',width=2,edge_color='blue')
plt.show()


# In[7]:


import networkx as nx
import matplotlib.pyplot as plt

g=nx.DiGraph()
g.add_nodes_from([0,1,2,3])

g.add_edge(0,3)
g.add_edge(3,0)
g.add_edge(0,1)
g.add_edge(1,3)
g.add_edge(2,0)
g.add_edge(3,2)
nx.draw_networkx(g,node_size=850,node_color='red',width=2,edge_color='blue')
plt.show()


# In[9]:


import networkx as nx
import matplotlib.pyplot as plt
g=nx.DiGraph()
l=[[1,0,0,1,0,1,1],[0,1,1,1,1,1,0],[1,1,1,0,1,0,1]]

g.add_nodes_from([0,1,2])

for i in range(0,3):
    for j in range(0,7):
        if l[i][j]==1:
            g.add_edge(i,j)
            
nx.draw(g,with_labels=True,node_size=1000,node_color='red',width=2,edge_color='blue')
plt.show()            


# In[10]:


import networkx as nx
import matplotlib.pyplot as plt
g=nx.DiGraph()
l=[[1,0,0,1,0,1,1],[0,1,1,1,1,1,0],[1,1,1,0,1,0,1],[1,0,0,1,0,1,1],[0,1,1,1,1,1,0],[1,1,1,0,1,0,1],[1,0,0,1,0,1,1]]

g.add_nodes_from([0,1,2])

for i in range(0,7):
    for j in range(0,7):
        if l[i][j]==1:
            g.add_edge(i,j)
            
nx.draw(g,with_labels=True,node_size=1000,node_color='red',width=2,edge_color='blue')
plt.show()            


# ## Plotly

# - plotly.express(the creator)
# - plotly.io(the manager)
# - pio.renderers.default='notebook'

# ## Bar Chart(Plotly)

# In[12]:


import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default='notebook'

data={
    "Department":["IT","IT","HR","HR","Finance","Finance"],
    "Gender":["Male","Female","Male","Female","Male","Female"],
    "Salary":[50000,-55000,45000,48000,70000,72000]
}

df=pd.DataFrame(data)
fig=px.bar(df,x='Department',y='Salary',title='Department Salary')
fig.show()


# In[14]:


import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default='notebook'

data={
    "Fruit":["Apples","Apples","Banana","Banana","Oranges","Oranges"],
    "City":["NYC","LA","NYC","LA","NYC","LA"],
    "Sales":[100,120,80,70,90,110],
    "Profit":[20,25,15,10,18,22],
    "Region":["East","West","East","West","East","West"]
}
fig=px.bar(data,
           x="Fruit",
           y="Sales",
           width=800,
           height=500,
           title="Fruit Sales Analysis",
           color="City",
           hover_data=["Profit","Region"],
           pattern_shape="City",
           barmode="group",
           text_auto=".2s",
           text="Sales",
           orientation="v",
          color_discrete_map={"NYC":"gold","LA":"midnightblue"},)
#           color_discrete_sequence=px.colors.qualitative.Pastel(Optional alternative)
fig.show()


# In[16]:


import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default='notebook'

data={
    "Fruit":["Apples","Apples","Banana","Banana","Oranges","Oranges"],
    "City":["NYC","LA","NYC","LA","NYC","LA"],
    "Sales":[100,120,80,70,90,110],
    "Profit":[20,25,15,10,18,22],
    "Region":["East","West","East","West","East","West"]
}
fig=px.bar(data,
           x="Fruit",
           y="Sales",
           width=800,
           height=500,
           title="Fruit Sales Analysis",
           color="City",
           hover_data=["Profit","Region"],
           pattern_shape="City",
           barmode="stack",
           text_auto=".2s",
           text="Sales",
           orientation="v",
          color_discrete_map={"NYC":"gold","LA":"midnightblue"},)
#           color_discrete_sequence=px.colors.qualitative.Pastel(Optional alternative)
fig.show()


# In[18]:


import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default='notebook'

data={
    "Fruit":["Apples","Apples","Banana","Banana","Oranges","Oranges"],
    "City":["NYC","LA","NYC","LA","NYC","LA"],
    "Sales":[100,120,80,70,90,110],
    "Profit":[20,25,15,10,18,22],
    "Region":["East","West","East","West","East","West"]
}
fig=px.bar(data,
           x="Fruit",
           y="Sales",
           width=800,
           height=500,
           title="Fruit Sales Analysis",
           color="City",
           hover_data=["Profit","Region"],
           pattern_shape="City",
           barmode="relative",
           text_auto=".2s",
           text="Sales",
           orientation="v",
          color_discrete_map={"NYC":"gold","LA":"midnightblue"},)
#           color_discrete_sequence=px.colors.qualitative.Pastel(Optional alternative)
fig.show()


# ## Scatter(Plotly)

# In[19]:


import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default='notebook'

data = {
    "Hours_Studied": [2,3,4,5,6,7,8,3,5],
    "Marks": [40,50,55,65,70,80,85,48,68],
    "Gender": ["Male","Female","Male","Female","Male","Female","Male",
               "Female","Male"],
    "Attendance": [60,70,75,80,85,90,95,72,88],
    "Department": ["IT","IT","HR","HR","Finance","Finance","IT","HR","Finance"]
}

df = pd.DataFrame(data)
fig = px.scatter(
    df,
    x="Hours_Studied",
    y="Marks",
    width=900,
    height=500,
    title="Student Performance Analysis",
    color="Gender",                 # grouping by color
    size="Attendance",              # bubble size
    color_discrete_map={
        "Male": "blue",
        "Female": "red"
    },
    
#     color_discrete_sequence=["blue","red"],

    symbol="Gender",                # different marker shapes
    
#     facet_col="Department",         # separate charts by column
#     facet_row="Gender"              # separate charts by row
)

fig.show()


# In[20]:


import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default='notebook'

data = {
    "Hours_Studied": [2,3,4,5,6,7,8,3,5],
    "Marks": [40,50,55,65,70,80,85,48,68],
    "Gender": ["Male","Female","Male","Female","Male","Female","Male",
               "Female","Male"],
    "Attendance": [60,70,75,80,85,90,95,72,88],
    "Department": ["IT","IT","HR","HR","Finance","Finance","IT","HR","Finance"]
}

df = pd.DataFrame(data)
fig = px.scatter(
    df,
    x="Hours_Studied",
    y="Marks",
    width=900,
    height=500,
    title="Student Performance Analysis",
    color="Gender",                 # grouping by color
    size="Attendance",              # bubble size
    color_discrete_map={
        "Male": "blue",
        "Female": "red"
    },
    
#     color_discrete_sequence=["blue","red"],

    symbol="Gender",                # different marker shapes
    
    facet_col="Department",         # separate charts by column
#     facet_row="Gender"              # separate charts by row
)

fig.show()


# In[21]:


import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default='notebook'

data = {
    "Hours_Studied": [2,3,4,5,6,7,8,3,5],
    "Marks": [40,50,55,65,70,80,85,48,68],
    "Gender": ["Male","Female","Male","Female","Male","Female","Male",
               "Female","Male"],
    "Attendance": [60,70,75,80,85,90,95,72,88],
    "Department": ["IT","IT","HR","HR","Finance","Finance","IT","HR","Finance"]
}

df = pd.DataFrame(data)
fig = px.scatter(
    df,
    x="Hours_Studied",
    y="Marks",
    width=900,
    height=500,
    title="Student Performance Analysis",
    color="Gender",                 # grouping by color
    size="Attendance",              # bubble size
    color_discrete_map={
        "Male": "blue",
        "Female": "red"
    },
    
#     color_discrete_sequence=["blue","red"],

    symbol="Gender",                # different marker shapes
    
#     facet_col="Department",         # separate charts by column
  facet_row="Gender"              # separate charts by row
)

fig.show()


# In[22]:


import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default='notebook'

data = {
    "Hours_Studied": [2,3,4,5,6,7,8,3,5],
    "Marks": [40,50,55,65,70,80,85,48,68],
    "Gender": ["Male","Female","Male","Female","Male","Female","Male",
               "Female","Male"],
    "Attendance": [60,70,75,80,85,90,95,72,88],
    "Department": ["IT","IT","HR","HR","Finance","Finance","IT","HR","Finance"]
}

df = pd.DataFrame(data)
fig = px.scatter(
    df,
    x="Hours_Studied",
    y="Marks",
    width=900,
    height=500,
    title="Student Performance Analysis",
    color="Gender",                 # grouping by color
    size="Attendance",              # bubble size
    color_discrete_map={
        "Male": "blue",
        "Female": "red"
    },
    
#     color_discrete_sequence=["blue","red"],

    symbol="Gender",                # different marker shapes
    
     facet_col="Department",         # separate charts by column
     facet_row="Gender"              # separate charts by row
)

fig.show()


# ## Scatter 3D(Plotly)

# In[24]:


import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default='notebook'

data={
    "Hours":[2,3,4,5,6],
    "Marks":[40,50,60,70,80],
    "Attendance":[60,65,70,80,90]
}
df=pd.DataFrame(data)
fig = px.scatter_3d(
    df,
    x="Hours",
    y="Marks",
    z="Attendance",
    color="Marks",
    title="3D Scatter Plot",
    size='Marks'
)

fig.show()


# In[25]:


import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default='notebook'

data={
    "Hours":[2,3,4,5,6],
    "Marks":[40,50,60,70,80],
    "Attendance":[60,65,70,80,90]
}
df = pd.DataFrame(data)
fig = px.scatter_matrix(
    df,
    dimensions=["Hours","Marks","Attendance"],
    color="Marks",
    title="Scatter Matrix",
    width=800,
    height=500
)

fig.show()


# ## LineChart

# In[28]:


import pandas as pd
import plotly.express as px

data = {
    "Month": ["Jan","Feb","Mar","Apr","Jan","Feb","Mar","Apr"],
    "Sales": [100,120,140,160,90,110,130,150],
    "Region": ["North","North","North","North",
               "South","South","South","South"]
}

df = pd.DataFrame(data)
fig = px.line(
    df,
    x="Month",
    y="Sales",
    color="Region",
    markers=True,
    width=800,
    height=500,
    title="Monthly Sales Comparison",
    color_discrete_sequence=["blue","red"]
)

fig.show()


# ## Histogram

# In[32]:


import pandas as pd
import plotly.express as px

data = {
    "Marks":[40,45,50,55,60,65,70,75,80,85],
    "Gender":["Male","Female","Male","Female","Male",
              "Female","Male","Female","Male","Female"]
}

df = pd.DataFrame(data)
fig = px.histogram(
    df,
    x="Gender",
    y='Marks',
    nbins=5,
    color="Gender",
    histfunc="sum",
    pattern_shape="Gender",
    text_auto=True,
    color_discrete_map={"Male":"blue","Female":"pink"},
#     color_discrete_sequence=["blue","pink"] #Optional
)

fig.show()


# In[33]:


import pandas as pd
import plotly.express as px

data = {
    "Marks":[40,45,50,55,60,65,70,75,80,85],
    "Gender":["Male","Female","Male","Female","Male",
              "Female","Male","Female","Male","Female"]
}

df = pd.DataFrame(data)
fig = px.histogram(
    df,
    x="Gender",
    nbins=5,
    color="Gender",
    histfunc="count",
    pattern_shape="Gender",
    text_auto=True,
    color_discrete_map={"Male":"blue","Female":"pink"},
#     color_discrete_sequence=["blue","pink"] #Optional
)

fig.show()


# In[34]:


import pandas as pd
import plotly.express as px

data = {
    "Marks":[40,45,50,55,60,65,70,75,80,85],
    "Gender":["Male","Female","Male","Female","Male",
              "Female","Male","Female","Male","Female"]
}

df = pd.DataFrame(data)
fig = px.histogram(
    df,
    x="Gender",
    nbins=5,
    color="Gender",
    histfunc="max",
    pattern_shape="Gender",
    text_auto=True,
    color_discrete_map={"Male":"blue","Female":"pink"},
#     color_discrete_sequence=["blue","pink"] #Optional
)

fig.show()


# ## Pie Chart(Plotly)

# In[35]:


import pandas as pd
import plotly.express as px

data = {
    "Department": ["IT", "HR", "Finance", "Marketing"],
    "Employees": [40, 20, 25, 15]
}

df = pd.DataFrame(data)
fig = px.pie(
    df,
    values="Employees",
    names="Department",
    color_discrete_sequence=["blue", "green", "orange", "red"],
    title="Employee Distribution by Department"
)

fig.update_traces(
    textinfo="percent+label",
    textposition="inside",
    pull=[0,0.1,0,0]
)
fig.show()


# In[ ]:




