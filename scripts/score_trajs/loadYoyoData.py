#!/usr/bin/python3

import pandas as pd
import os.path as osp

def load_dataframe(file_format,file_path):
   """
   (str,str) -> pandas.dataframe
   Given a file_format (i.e., csv or h5) and path, attempt
   to load and return a data frame. If file path doesn't exist
   or file file_format is not csv or h5, then return None.
   """
   if(not osp.isfile(file_path)):
      print("(!) ERROR: "+file_path+" does not exist.")
      return None

<<<<<<< HEAD:scripts/loadYoyoData.py
   print("loading: "+file_path)
=======
   print("loading: "+fpath)
>>>>>>> SpaceKitKat/master:scripts/score_trajs/loadYoyoData.py

   if(file_format == 'csv'):
      dt = pd.read_csv(file_path,delimiter=',')
   elif(file_format == 'h5'):
      # get name of data set by file name
      filename = file_path.split('/')[-1]
      dt = pd.read_hdf(file_path,filename.split('.')[0])
   else:
      print("(!) load_data: file file_format, "+file_format+", is unrecognized.")
      dt = None

<<<<<<< HEAD:scripts/loadYoyoData.py

=======
>>>>>>> SpaceKitKat/master:scripts/score_trajs/loadYoyoData.py
   return dt

def save_dataframe(data_frame,file_format,file_path):
   """
   (str,str,pandas.dataframe) -> None
   Save a data frame according to file format (cvs or hdf) at the
   given file path. Throws if file path doesn't exist.
   """
   filename = file_path.split('/')[-1]
   file_location = file_path.replace(filename,"")
   if (not osp.exists(file_location)):
      raise EXCEPTION("Filepath doesn't exist")

   if (file_format == 'csv'):
      data_frame.to_csv(file_path,index=False)
   else:
      print("(!) save_data: file file_format, "+file_format+", is unrecognized.")

   return