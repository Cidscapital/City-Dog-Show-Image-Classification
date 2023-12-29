#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Jesse Jason
# DATE CREATED: 10/11/2023                                  
# REVISED DATE: 
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

# Define the get_input_args function
def get_input_args():
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()

    # Create 3 command line arguments as mentioned above using add_argument() from ArgumentParser method
    parser.add_argument('--dir', type=str, default='pet_images/', help='path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg', help='CNN model architecture (e.g., vgg, resnet, etc.)')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='text file containing dog names')

    # Replace None with parser.parse_args() parsed argument collection that 
    # you created with this function 
    return parser.parse_args()

# Example usage:
# in_args = parser.parse_args()

# print("Argument 1:", in_args.dir)
# print("Argument 2:", in_args.arch)
# print("Argument 2:", in_args.dogfile)
