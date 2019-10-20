#Android Application Graph Signature 
# © Created By - Devyani Vij and Riya Khan
#Header Files
import optparse
import networkx as nx
import re
import matplotlib.pyplot as plt
import pylab
import warnings
import os
import glob
import fnmatch
import pyfiglet
import warnings

warnings.filterwarnings("ignore")

#Android Application Graph Signature ASCII Banner
ascii_banner = pyfiglet.figlet_format("Android \t Application \t Graph \t Signature",width=1000)
print(ascii_banner)

#Reading the Callgraphs created using androguard tool
G2 = nx.read_gml('callgraph.gml',label='label') 

#List containing the names of all the sensitive API without their methods. 
sensitive_api=['TelephonyManager','SmsManager','LocationManager','AudioManager','HttpURLConnection','ConnectivityManager','BroadcastReceiver','Cipher','AccessibleObject','PackageManager']

sensitive_api_malware=[]

count_api_in_malware = 0

#Using Regex to fetch all the sensitive API calls from the call graphs and counting the TOTAL number of sensitive API in Application
for j in sensitive_api:
    for i in G2.nodes():
        data = re.split('[;]',i)
        data1 = re.split('/',data[0])
        for k in data1:
            if k in sensitive_api:
                if i in sensitive_api_malware:
                    continue
                else:
                    sensitive_api_malware.append(i)
                    count_api_in_malware=count_api_in_malware+1

print('\033[93m'+"Total Sensitive API Calls found in the MALWARE: "+str(count_api_in_malware))

#Reading the graph of the Application 
G = nx.read_gml('callgraph.gml',label='id')

data=[]

b=nx.get_node_attributes(G,'label')

for keys,values in b.items():
    splitting = re.split('[[]',values)
    if splitting[0] in sensitive_api_malware:
        data.append(keys)

#Getting the CALLER and CALLEE relationship between the Sensitive API's fetched above.
listing=[]
U = nx.DiGraph()
counter_in_degree=0
for i in data:
        
        a=G.in_edges(i)
        for j in a:
            b=list(j)
            for k in b:
                if k in data:
                    if G.nodes[k]['label'] not in listing:
                        listing.append(G.nodes[k]['label'])
                        counter_in_degree=counter_in_degree+G.in_degree(i)
                    else:
                        continue
                else:
                    continue

#Sorting the API names in ascending order to construct a DiGraph showing a relation between caller and callee.
sensitive_api_in_malware_name=[]
for el in sorted(listing):
    sensitive_api_in_malware_name.append(el)
    
#Printing the Sensitive API calls found and Creating the DiGraph for sensitive API calls with the API's calling them
print("\n\nSensitive API calls are:")
for i in range(0,len(sensitive_api_in_malware_name)):
    for j in data:
        if G.nodes[j]['label']==sensitive_api_in_malware_name[i]:
            print('\033[96m'+sensitive_api_in_malware_name[i])
            a=G.in_edges(j)
            H=nx.DiGraph(a)
            break
        else:
            continue
    U = nx.disjoint_union(U, H)
    
b=[]
print("\n\n\n\033[93mCaller - Callee Relationship:")

for i in range(0,len(sensitive_api_in_malware_name)):
    for j in data:
        if G.nodes[j]['label']==sensitive_api_in_malware_name[i]:
            print('\n\033[93m'+'CALLEE -'+'\n\033[96m'+sensitive_api_in_malware_name[i])
        
            a=G.in_edges(j)
            if(len(a)==0):
                continue
            else:
                print('\033[93m'+'CALLER -')
                for j in a:
                    b=list(j)
                    for k in b:
                        if k not in data:
                            print('\033[96m'+G.nodes[k]['label'])
                        else:
                            continue

nx.write_gml(U, "Signature.gml")
#Plotting the Graph
nx.draw(U,arrows=True,with_labels=True,edge_color = 'b')
plt.show()
print("\n")     
