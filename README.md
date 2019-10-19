# Android Malware Signature Creator

<!-- Library Logo -->
<img src="https://github.com/devu-62442/Android_Malware_Signature_Creator/blob/master/img/google_android_root_0.png" align="left" hspace="1" vspace="1">

<!-- Buy me a cup of coffe -->
<a href='https://ko-fi.com/A406JCM' style='margin:13px;' target='_blank' align="right"><img align="right" height='36' src='https://az743702.vo.msecnd.net/cdn/kofi4.png?v=f' alt='Buy Me a Coffee at ko-fi.com' /></a>
<a href='https://play.google.com/store/apps/details?id=com.vansuita.materialabout.sample&pcampaignid=MKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1' target='_blank' align="right"><img align="right" height='36' src='https://s20.postimg.org/muzx3w4jh/google_play_badge.png' alt='Get it on Google Play' /></a>
# Material About


This is an [**Android**](https://developer.android.com) project. You, as a mobile developer, can use this library to show a material about screen in your apps.
It was built to make your life easier when introducing you to your users, and also, to create an about screen pattern for material android apps. It's really simple and dynamic, check it out.

</br>

##### Note: If you're missing some feature please let me know. Or even better, create a pull request. Also, I'm needing some help to translate the strings.xml to other languages.

##### Supported Languages: 🇺🇸 🇧🇷 🇪🇸 🇮🇹 🇷🇺 🇩🇪 :cn: :tr: 🇺🇦 🇫🇷 🇦🇪 🇰🇷

</br>

<!-- JitPack integration -->
[![JitPack](https://jitpack.io/v/jrvansuita/MaterialAbout.svg)](https://jitpack.io/#jrvansuita/MaterialAbout)
[![Android Arsenal](https://img.shields.io/badge/Android%20Arsenal-MaterialAbout-green.svg?)](https://android-arsenal.com/details/1/4614) [![MaterialUp](https://img.shields.io/badge/MaterialUp-MaterialAbout-6ad0d9.svg?)](https://www.uplabs.com/posts/material-about) [![ghit.me](https://ghit.me/badge.svg?repo=jrvansuita/MaterialAbout)](https://ghit.me/repo/jrvansuita/MaterialAbout)

# Sample app
 This library has a lot more customization and features than is able to show here. Please check the sample app and feel free to help with a pull request. You can take a look at the sample app [located on this project](/app/).

<img src="images/screenshots/dark.jpg" height='auto' width='270'/><img src="images/screenshots/light.jpg" height='auto' width='270'/><img src="images/screenshots/custom.jpg" height='auto' width='270'/>

[![Appetize.io](https://img.shields.io/badge/Apptize.io-Run%20Now-brightgreen.svg?)](https://appetize.io/embed/3b4dpd5kv90mpa67mp5h8mugc0?device=nexus7&scale=50&autoplay=true&orientation=portrait&deviceColor=black) [![Demo](https://img.shields.io/badge/Demo-Download-blue.svg)](http://apk-dl.com/dl/com.vansuita.materialabout.sample) 
 [![Codacy Badge](https://api.codacy.com/project/badge/Grade/118bb89e3bed43e2b462201654224a60)](https://www.codacy.com/app/jrvansuita/MaterialAbout?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jrvansuita/MaterialAbout&amp;utm_campaign=Badge_Grade) 
 <a target="_blank" href="https://developer.android.com/reference/android/os/Build.VERSION_CODES.html#GINGERBREAD"><img src="https://img.shields.io/badge/API-9%2B-blue.svg?style=flat" alt="API" /></a>


# Setup

This library requires `minSdkVersion` to be set to `14` or above, like the [Official Support Library](https://developer.android.com/topic/libraries/support-library/index.html#api-versions).

#### Step #1. Add the JitPack repository to your build file:

```gradle
allprojects {
    repositories {
	...
	maven { url "https://jitpack.io" }
    }
}
```

#### Step #2. Add the dependency ([See latest release](https://jitpack.io/#jrvansuita/MaterialAbout)).

```groovy
dependencies {
       compile 'com.github.jrvansuita:MaterialAbout:+'
}
```
# Implementation

Create a [AboutView](/library/src/main/java/com/vansuita/materialabout/views/AboutView.java) instance with [AboutBuilder](/library/src/main/java/com/vansuita/materialabout/builder/AboutBuilder.java).
```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    AboutView view = AboutBuilder.with(this)
                 .setPhoto(R.mipmap.profile_picture)
                 .setCover(R.mipmap.profile_cover)
                 .setName("Your Full Name")
                 .setSubTitle("Mobile Developer")
                 .setBrief("I'm warmed of mobile technologies. Ideas maker, curious and nature lover.")
                 .setAppIcon(R.mipmap.ic_launcher)
                 .setAppName(R.string.app_name)
                 .addGooglePlayStoreLink("8002078663318221363")
                 .addGitHubLink("user")
                 .addFacebookLink("user")
                 .addFiveStarsAction()
                 .setVersionNameAsAppSubTitle()
                 .addShareAction(R.string.app_name)
                 .setWrapScrollView(true)
                 .setLinksAnimated(true)
                 .setShowAsCard(true)
                 .build();

    addContentView(view, layoutParams);
}
```


# Additional

### Getting the list of actions or links from AboutBuilder.

```java
AboutBuilder aboutBuilder = AboutBuilder.with(this);

List<Item> actions = aboutBuilder.getActions();
List<Item> links = aboutBuilder.getActions();
```


#### Getting the view instance of any action or link from AboutView?

```java
AboutView view = AboutBuilder.with(this)
                 ...
                 .build();

View lastLinkView = view.findItem(builder.getLastLink());
View lastActionView = view.findItem(builder.getLastAction());
```

# Used libraries

* [com.android.support:appcompat-v7](https://developer.android.com/topic/libraries/support-library/packages.html#v7-appcompat)
* [com.android.support:cardview-v7](https://developer.android.com/topic/libraries/support-library/packages.html#v7-cardview)
* [com.github.jrvansuita:IconHandler](https://github.com/jrvansuita/IconHandler)

#

<a href="https://plus.google.com/+JuniorVansuita" target="_blank">
  <img src="https://s20.postimg.org/59xees8vt/google_plus.png" alt="Google+" witdh="44" height="44" hspace="10">
</a>
<a href="https://www.linkedin.com/in/arleu-cezar-vansuita-júnior-83769271" target="_blank">
  <img src="https://s20.postimg.org/vxoeax4ah/linkedin.png" alt="LinkedIn" witdh="44" height="44" hspace="10">
</a>
<a href="https://www.instagram.com/jnrvans/" target="_blank">
  <img src="https://s20.postimg.org/lyyuap5h5/instagram.png" alt="Instagram" witdh="44" height="44" hspace="10">
</a>
<a href="https://github.com/jrvansuita" target="_blank">
  <img src="https://s20.postimg.org/jf37glhx5/github.png" alt="Github" witdh="44" height="44" hspace="10">
</a>
<a href="https://play.google.com/store/apps/dev?id=8002078663318221363" target="_blank">
  <img src="https://s20.postimg.org/5iuz4plo9/android.png" alt="Google Play Store" witdh="44" height="44" hspace="10">
</a>
<a href="mailto:vansuita.jr@gmail.com" target="_blank" >
  <img src="https://s20.postimg.org/slli3vn5l/email.png" alt="E-mail" witdh="44" height="44" hspace="10">
</a>



## Android Malware detection through Network Traffic Analysis
Android is a Linux based operating system it is designed primarily for touch screen mobile devices such as smartphones and tablet computers. The operating system have developed a lot in last 15 years starting from black and white phones to recent smartphones or mini computers. One of the most widely used mobile OS these days is android. The android is software that was founded in Palo Alto of California in 2003. Android has been the best-selling OS worldwide on smartphones since 2011 and on tablets since 2013. As of May 2017, it has over 2 billion monthly active users, the largest installed base of any operating system, and as of December 2018, the Google Play store features over 2.6 million apps.

Growing popularity of Android mobile operating system has not only attracted user community but also the malware developers towards this platform. Large number of malicious apps have been detected in the past years in Google Play Store and third party app markets.

## Getting Started

Many detection techniques have been proposed in the for Android malware detection :

    - Based on Permissions  
    - Based on System Calls  
    - Signature Based.

We used a detection technique based on network traffic analysis. We compare network traffic of malwares with that of benign apps and find the features which distinguish both types of traffic. Based upon these features we build a decision tree classifier to detect benign and malicious apps from the testing dataset. Network traffic analysis main objective is to :

    -: Analyse the traffic flowing across the network. 

    -: Analysis the traffic to detect the unwanted traffic being used by a particular application.

    -: Network traffic analysis to catch the Behavioral Patterns for Spotting Suspicious Activities

    -: Analysis of traffic to minimise damages caused by the malicious applications (or apps) 

### There are many reasons why network traffic analysis is good for detection of android malware some of them are :

   &#x1F538; - Network Traffic Analysis gives you in-depth application monitoring and bandwidth utilisation capabilities.           
   
   &#x1F538; - With network traffic analysis for netflow, you can produce reports that show use of unwanted traffic.
   
   &#x1F538; - Network Traffic Analysis gives you a ready tool for a quick deep dive into the underlying causes of network slowdowns.
   
   &#x1F538; - Pattern can be noted that had persisted for a couple of hours. Network Traffic Analysis shows how these patterns are  affecting the system.
  
The proposed model classifies a given apk as malware or benign based on a dynamic analysis of the network traffic generated by it. There are three phases to this operation and are explained as follows: 

 Step 1 - Data Collection : 
          The first phase focuses on gathering benign and malware apps which are then installed into an emulator and is 
          launched manually. Then we use tcpdump to dump the raw traffic data into a pcap file.
 
 Step 2 - Feature Extraction and Labelling : 
          The second phase involves feature extraction where we open the pcap file in wireshark and calculate the feature 
          values used for our dataset and create a csv file consisting of the required features and a label indicating which 
          apps are malware. 
 
 Step 3 - Training and Testing : 
          In the last phase we feed the csv file into a machine learning model where a part of the data set is used to train 
          the model and the rest is for testing. 
￼
 
# WORKING
We start with capturing network traffic of malicious as well as benign (normal) apps. We used -
### Android Studio Emulator QEMU 
which acts as a dummy Android Phone where the benign as well as malware applications can be installed. We are using 
### QVGA 2.7’’ android device with Android Jelly Bean 4.1 version. 

![alt text](https://github.com/devu-62442/Android-Malware-Analysis/blob/master/images/Screenshot%202019-07-24%20at%2010.16.06%20AM.png)

From the dataset of Android malware samples we take one by one a malicious sample,install it on the phone through adb command 
### ( adb install Application-Name ) 

![alt text](https://github.com/devu-62442/Android-Malware-Analysis/blob/master/images/image-1.png)

and run the application on the android emulator then use the tcpdump command 
### ( tcpdump -w Application-Name ) 

![alt text](https://github.com/devu-62442/Android-Malware-Analysis/blob/master/images/Screenshot%202019-07-24%20at%2010.16.20%20AM.png)

to capture the application traffic. These all commands can run through the command line ( command prompt ). 

The data captured is now mined. Data mining is the process of extraction of relevant information from a collection of data. Mining of a particular information related to a concept is done on the basis of the feature of the data.
	
Next step is the feature selection step. 

![alt text](https://github.com/devu-62442/Android-Malware-Analysis/blob/master/images/Screenshot%202019-07-24%20at%2010.40.42%20AM.png)

Feature selection is critical to building a good model for several reasons. 

- One is that feature selection implies some degree of cardinality reduction, to impose a cutoff on the number of attributes that can be considered when building a model. 

- Data almost always contains more information than is needed to build the model, or the wrong kind of information. 

- Not only does feature selection improve the quality of the model, it also makes the process of modeling more efficient. 

We selected the following network traffic features which we compared with both types of traffic. These traffic features are selected based upon the information gain, the higher the information gain the more information it can give us. So that attribute is selected as a feature. 

![alt text](https://github.com/devu-62442/Android-Malware-Analysis/blob/master/images/Screenshot%202019-07-24%20at%2010.41.30%20AM.png)

After capturing traffic from both malicious and normal apps we start analysis of traffic in terms of network traffic features.
Through Wireshark - 

![alt text](https://github.com/devu-62442/Android-Malware-Analysis/blob/master/images/Screenshot%202019-07-24%20at%2010.41.57%20AM.png)

Next we create a .csv file (dataset) including the data for each and every feature for a particular application and adding a tag (label) mentioning it is a malware or not.

![alt text](https://github.com/devu-62442/Android-Malware-Analysis/blob/master/images/Screenshot%202019-07-24%20at%2010.42.27%20AM.png)

Next step is to work on the machine learning algorithm. In our project we are using decision tree J48. 
The general motive of using Decision Tree is to create a training model which can be used to predict class or value of target variables by learning decision rules inferred from prior data (training data). The training set contains 60% of the data.

![alt text](https://github.com/devu-62442/Android-Malware-Analysis/blob/master/images/Screenshot%202019-07-24%20at%2010.42.39%20AM.png)

After training the data, the next step is to input our test set which is 40% of the total applications into the algorithm decision tree J48 which is an algorithm provided by the WEKA tool to predict the output from the test set and check the accuracy of the predicted set provided as an input against the training set.

![alt text](https://github.com/devu-62442/Android-Malware-Analysis/blob/master/images/Screenshot%202019-07-24%20at%2010.42.49%20AM.png)
![alt text](https://github.com/devu-62442/Android-Malware-Analysis/blob/master/images/Screenshot%202019-07-24%20at%2010.43.01%20AM.png)

Decision tree will also give a binary tree representation for a clearer and a diagrammatic based understanding of the classifications (predictions) it has done. 

According to the algorithm of the decision tree, the attribute (feature) which has the highest information gain becomes the root. Decision tree evaluates and finds the data for splitting.

![alt text](https://github.com/devu-62442/Android-Malware-Analysis/blob/master/images/Screenshot%202019-07-24%20at%2010.43.15%20AM.png)!

![alt text](https://github.com/devu-62442/Android-Malware-Analysis/blob/master/images/Screenshot%202019-07-24%20at%2010.43.24%20AM.png)

On each iteration of the algorithm, it iterates through every unused attribute of the test data set (T) and calculates the entropy (or information gain) of that attribute. It then selects the attribute which has the smallest entropy (or largest information gain) value. The set (T) is then split or partitioned by the selected attribute to produce subsets of the data. For example, a node can be split into child nodes based upon the subsets of the malware (label in our dataset). The algorithm continues to recur on each subset. 

![alt text](https://github.com/devu-62442/Android-Malware-Analysis/blob/master/images/Screenshot%202019-07-24%20at%2010.43.33%20AM.png)


