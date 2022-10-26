# Literature Data Mining (LDM): A Guide for Automatically Downloading and Highlighting Literature on Mass

This program is designed to help you to data mine the literature. There are several components to this tutorial

**Part 1**
* Installation of VirtualBox and downloading virtual machine containing the LDM Program
* Using VirtualBox and opening the Virtual Machine
* Preparing the Literature Data Mining (LDM) Program and Shared Folder in LDM Virtual Machine

**Part 2**
* Running the LDM program in the Virtual Machine

**If you are attending a tutorial based on learning literature data mining, make sure you have done everything in part 1 before the tutorial session.**

# Table of Contents

<!--ts-->
   * [Part 1: Setting up VirtualBox and the LDM Program](#part-1-setting-up-virtualbox-and-the-ldm-program)
      * [1. Installation](#1-installation)
         * [1.1: Install VirtualBox](#11-install-virtualbox)
         * [1.2: Download the LDM Virtual Machine](#12-download-the-ldm-virtual-machine)
      * [2. Using VirtualBox and opening the Virtual Machine](#2-using-virtualbox-and-opening-the-virtual-machine)
         * [2.1: Adding the LDM Virtual Machine to your VirtualBox](#21-adding-the-ldm-virtual-machine-to-your-virtualbox)
         * [2.2: Setting Up the Shared Folder](#22-setting-up-the-shared-folder)
         * [2.3: Starting Up the LDM Virtual Machine](#23-starting-up-the-ldm-virtual-machine)
      * [3. Preparing the Literature Data Mining (LDM) Program and Shared Folder in LDM Virtual Machine](#3-preparing-the-literature-data-mining-ldm-program-and-shared-folder-in-ldm-virtual-machine)
         * [3.1: Update the Literature Data Mining (LDM) Program](#31-update-the-literature-data-mining-ldm-program)
         * [3.2: Preparing the shared folder to access from the virtual machine](#32-preparing-the-shared-folder-to-access-from-the-virtual-machine)

   * [Part 2: Running the Literature Data Mining (LDM) Program](#part-2-running-the-literature-data-mining-ldm-program)
      * [4. Running the LDM program in the Virtual Machine](#4-running-the-ldm-program-in-the-virtual-machine)
<!--te-->

# Part 1: Setting up VirtualBox and the LDM Program

## 1. Installation

### 1.1: Install VirtualBox

To use the LDM, we will be using VirtualBox. VirtualBox is a program that allows you to run an operating system within your computer. This program is very useful if you can only run a program in certain operating systems. You will need to install this program on your computer. 

See https://www.virtualbox.org/wiki/Downloads to download and install VirtualBox on your computer. 

### 1.2: Download the LDM Virtual Machine

We will now download the LDM virtual machine to your computer. This virtual machine contains a version of Ubuntu (Linux) that we will run the LDM on. 

Download this virtual machine by downloading the contents from this OneDrive link onto your computer (You will ne about 20 GB of space on your computer. Make sure you have a good internet link when downloading this file): https://vuw-my.sharepoint.com/:f:/g/personal/wealge_staff_vuw_ac_nz/Epbk95CbqRNOm_iSvEVcy7cBlmXJzTJRtMEsAGnkH39Ljw?e=BoigGO

## 2. Using VirtualBox and opening the Virtual Machine

### 2.1: Adding the LDM Virtual Machine to your VirtualBox

First, we will add the LDM virtual machine to your VirtualBox:

1. Open the VirtualBox program.
2. Click the green + icon called add.

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/Add_to_VirtualBox.png">
</p>

3. Open the LDM.vbox file in VirtualBox.

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/Open_Virtual_Machine_original.png">
</p>

You have now added the LDM virtual machine to your VirtualBox. You will see the LDM in your VirtualBox list of virtual machines.

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/Open_Virtual_Machine_1_original.png">
</p>

### 2.2: Setting Up the Shared Folder 

We will now set up a folder on your computer that we will be working in. This folder will allow us to add data to the virtual machine, manipulate data, and copy data and pdf files from the LDM program.

1. Click on the LDM virtual machine and then click the orange :low_brightness: icon called Settings.

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/Open_Settings.png">
</p>

2. Click on the Shared Folders icon

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/Shared_Folders_1.png">
</p>

3. Click the folder button as shown below:

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/Shared_Folders_2.png">
</p>

4. Click the <kbd>Down</kbd> button, then click the Other... button

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/Shared_Folders_3.png">
</p>

5. Create a new folder on your computer where you want to obtain pdf files from. Here, I have created a folder called `LDM_Shared_Folder` on my computer. Then click `Open`.

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/shared_folder_original_3.png">
</p>

6. Finally, click the `OK` button. 

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/Shared_Folders_4_2.png">
</p>

The shared folder between you computer and the LDM virtual machine has now been created. 

### 2.3: Starting Up the LDM Virtual Machine

We will now turn on the LDM Virtual Machine. Click on the LDM virtual machine and then click the green &rarr icon called show.

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/Start_LDM_Virtual_Machine_vertical.png">
</p>

A new window contains the LDM virtual machine will now begin. This will look like a computer is turning on. It is ready when the virtual machine looks like below:

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/Started_VM.png">
</p>



## 3. Preparing the Literature Data Mining (LDM) Program and Shared Folder in LDM Virtual Machine.

We now have set up the LDM Virtual Machine. We not need to prepare this virtual machine before we begin literature mining.

### 3.1: Update the Literature Data Mining (LDM) Program

Before beginning, we will update the LDM program. To do this, we will first open a terminal, where we will be doing all our work.

1. Click on the Terminal icon. See the image below. This will open a new terminal.

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/Shared_Folder_VM_Fix.png">
</p>

2. In the terminal, type the following line and then press the `Enter` button: ``update_ldm``

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/update_ldm_1.png">
</p>

3. This will then update the LDM program, as well as any other programs that are needed. You will see code like this appear in the terminal:

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/update_ldm_2.png">
</p>

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/update_ldm_3.png">
</p>

4. Once this has finished, you are all done. You can now quit the terminal by clicking the `x` button at the top right-hand corner of the terminal. See the images below:

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/update_ldm_exit.png">
</p>

### 3.2: Preparing the shared folder to access from the virtual machine

Now, we need to give our virtual machine the permissions to access the shared folder, otherwise we will see this error box displayed:

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/Shared_Folder_VM_Error.png">
</p>

If you ever see this error, do the following:

1. Click on the Terminal icon. See the image below. This will open a new terminal.

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/Shared_Folder_VM_Fix.png">
</p>

2. In the terminal, type the following line and then press the `Enter` button: ``sudo adduser $USER vboxsf``

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/Shared_Folder_VM_Fix_2.png">
</p>

3. The terminal will ask to put the password for the virtual machine in. This is ``ldm``. Type this in and then press the `Enter` button. 

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/Shared_Folder_VM_Fix_3.png">
</p>

4. You will now see the following message. Now quit the terminal by clicking the `x` button at the top right-hand corner of the terminal, then restart the LDM virtual machine. See the images below:

<p align="center">
	<img src="https://github.com/geoffreyweal/LDM/blob/main/Images/Using_VirtualBox/Restart_after_shared_VM.png">
</p>

Once the virtual machine has restarted, you will now be able to access the shared folder, which will be important for this exercise.

# Part 2: Running the Literature Data Mining (LDM) Program

## 4. Running the LDM program in the Virtual Machine







