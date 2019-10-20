# Android Application Graph Signature 

<!-- Library Logo -->
<img src="https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/google_android_root_0.png" align="left" hspace="1" vspace="1">

<img align="right" height='50' src='https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/dims.jpeg' alt='Buy Me a Coffee at ko-fi.com' /></a>

## Android 
[**Android**](https://developer.android.com) is a Linux based operating system it is designed primarily for touch screen mobile devices such as smartphones and tablet computers. One of the most widely used mobile OS these days is android. The android is software that was founded in Palo Alto of California in 2003. As of May 2017, it has over 2 billion monthly active users, the largest installed base of any operating system, and as of December 2018, the Google Play store features over 2.6 million apps.

Growing popularity of Android mobile operating system has not only attracted user community but also the malware developers towards this platform. Large number of malicious apps have been detected in the past years in Google Play Store and third party app markets.
</br>

<!-- Packages Used -->
![Python](https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f6e6574776f726b782e737667-2.svg)
![Python](https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/68747470733a2f2f7472617669732d63692e6f72672f6e6574776f726b782f6e6574776f726b782e7376673f6272616e63683d6d6173746572.svg) ![Python](https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/68747470733a2f2f63692e6170707665796f722e636f6d2f6170692f70726f6a656374732f7374617475732f6769746875622f6e6574776f726b782f6e6574776f726b783f6272616e63683d6d6173746572267376673d74727565.svg)
![Networkx](https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/networkx.svg)
![Matplotlib](https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/matplotlib.svg)

</br>
<a href='http://networkx.github.io'><img align='left' height='50' src='https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/networkx_logo_1.png' /></a>

<a href='https://matplotlib.org'><img align='right' height='30' src='https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/logo2.png' /></a>

## - Android Application Graph Signature Creator -

<img align='center' height='83' src='https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/Screenshot%202019-10-20%20at%2010.27.53%20PM.png' />
Applications in Android Store (or the App Store) are in billions. A user is not able to know whether it's a benign App or not. So to detect whether an Application is Benign or Malware it should be uniquely identified which are termed as signatures of the application.

Android Malware are the malwares which have infected Android in many differet ways. Each malware have a different structure and executions. The malwares which behave similarly are categorised into a single Android Malware Family. 

## API 
APIs are a set of functions and procedures that allow for the creation of applications that access data and features of other applications, services or operating system. APIs makes it easier to develop a computer program by providing all the building blocks, which are then put together by the programmer. With an API, you really don’t know what’s going on behind the scenes. In other words, an API is the messenger that delivers your request to the provider that you’re requesting it from and then delivers the response back to you.

Android is divided into a layered architecture. Application  framework  layer  is  on  top  of  native library layer. The application layer provides major Application  programming  interface  (APIs)  and higher-level services in the form of java classes. The application developers are allowed to access all the APIs framework  for  the  core  programs that  make simpler the reuse of APIs components. These APIs are open to everybody to create android applications. There is different type  of application  components. Each type has a different lifecycle and purpose that describes how the  component  will be  created and destroyed. Frameworks in the Application Framework layer are written in Java and provide abstractions of the underlying native libraries and Dalvik capabilities to applications. Android applications run in their own sandboxed Dalvik VM and can consist of multiple components: Activities, services, broadcast receivers and content providers etc. Components can interact with other components of the same or a different application via intents. 

## Sensitive API


## Callgraphs
A call graph (also known as a call multigraph) is a control flow graph, which represents calling relationships between API's in an Android Application. Each node represents an API and each edge (f, g) indicates that API a calls API b. Call graphs can be dynamic or static.A dynamic call graph is a record of an execution of the Android Application. Thus, a dynamic call graph can be exact, but only describes one run of the application. A static call graph is a call graph intended to represent every possible execution of the Android Application.

Call graphs can be defined to represent varying degrees of precision. A more precise call graph more precisely approximates the behavior of the real Android Application, at the cost of taking longer to compute and more memory to store. The most precise call graph is fully context-sensitive, which means that for each application, the graph contains a separate node for each call stack that application have in it

## Working
Written in python ![Python](https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f6e6574776f726b782e737667-2.svg). ```It's used to create a UNIQUE directed graph as a signature```. The tool follows the following steps :-

#### Step #1. Use Androguard to create a callgraph :
```gradle
androguard cg 'Application Name'
```
<img align='right' height='200' src='https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/Screenshot%202019-10-20%20at%2010.31.34%20PM.png' />

</br>
A callgraph.gml is created using the above command in the same folder where application is placed.

#### Step #2. Create the signature :
Run the ```Signatue_Creator.py``` through command line. The Signatue_Creator.py is used to gather the API, using the callgraph.gml created in Step 1. The callgraphs contains around thousands of API's, from these only sensitive API's and the API's calling them are collected and represented as a directed graph. Each graph is unique for the family they belong too.

```gradle
python3 Signature_Creator.py
```

<img align='center' height='700' src='https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/Screenshot%202019-10-20%20at%2011.11.03%20PM.png' />
The sensitive API calls of a particular application is collected with a help of a list which contains all the sensitive API's names and is used to compare whther the API's are sensitive or not

```gradle
sensitive_api=['TelephonyManager','SmsManager','LocationManager','AudioManager','HttpURLConnection','ConnectivityManager','BroadcastReceiver','Cipher','AccessibleObject','PackageManager']
```
```A graph is created, displayed on the screen and saved as Signature.gml```
</br>
<img align='center' height='500' src='https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/Screenshot%202019-10-20%20at%2011.11.49%20PM.png' />
