<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>857</width>
    <height>479</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTextEdit" name="year">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>30</y>
      <width>161</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QTextEdit" name="month">
    <property name="geometry">
     <rect>
      <x>380</x>
      <y>30</y>
      <width>161</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QTextEdit" name="day">
    <property name="geometry">
     <rect>
      <x>630</x>
      <y>30</y>
      <width>181</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="yy">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>40</y>
      <width>61</width>
      <height>20</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="layoutDirection">
     <enum>Qt::RightToLeft</enum>
    </property>
    <property name="text">
     <string>Year</string>
    </property>
    <property name="textFormat">
     <enum>Qt::AutoText</enum>
    </property>
   </widget>
   <widget class="QLabel" name="mm">
    <property name="geometry">
     <rect>
      <x>296</x>
      <y>40</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="layoutDirection">
     <enum>Qt::RightToLeft</enum>
    </property>
    <property name="text">
     <string>Month</string>
    </property>
    <property name="textFormat">
     <enum>Qt::AutoText</enum>
    </property>
   </widget>
   <widget class="QLabel" name="dd">
    <property name="geometry">
     <rect>
      <x>566</x>
      <y>40</y>
      <width>51</width>
      <height>20</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="layoutDirection">
     <enum>Qt::RightToLeft</enum>
    </property>
    <property name="text">
     <string>Day</string>
    </property>
    <property name="textFormat">
     <enum>Qt::AutoText</enum>
    </property>
    <property name="scaledContents">
     <bool>false</bool>
    </property>
   </widget>
   <widget class="QPushButton" name="calculer">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>120</y>
      <width>791</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Calculate</string>
    </property>
   </widget>
   <widget class="QLabel" name="afficher">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>230</y>
      <width>791</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>36</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="frameShape">
     <enum>QFrame::WinPanel</enum>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="afficher_2">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>350</y>
      <width>791</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>36</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="frameShape">
     <enum>QFrame::WinPanel</enum>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="mm_2">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>200</y>
      <width>781</width>
      <height>20</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="layoutDirection">
     <enum>Qt::RightToLeft</enum>
    </property>
    <property name="text">
     <string>AGE</string>
    </property>
    <property name="textFormat">
     <enum>Qt::AutoText</enum>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="mm_3">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>320</y>
      <width>791</width>
      <height>20</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="layoutDirection">
     <enum>Qt::RightToLeft</enum>
    </property>
    <property name="text">
     <string>NEXT BIRTHDAY</string>
    </property>
    <property name="textFormat">
     <enum>Qt::AutoText</enum>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>857</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
