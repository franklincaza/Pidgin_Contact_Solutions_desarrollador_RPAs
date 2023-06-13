import requests
import unicodedata
import pandas as pd


r=("https://pidgin.nyc3.digitaloceanspaces.com/coderbyte/python_tests/test1_0.tsv")
url=r

def ejercicio(url): # NO MODIFIQUE ESTA LÍNEA

  resultado = ""

  r = requests.get(url)
  with open("index.tsv", "wb") as f:
      f.write(r.content)
      
  r.close()

  resultado =[{
      
      'nconst':'',
      'primaryName':'',	
      'birthYear':'',
      'deathYear':'',
      'primaryProfession':'',
      'knownForTitles':''	

  }]


  nconst=[]
  primaryname=[]
  birthYear=[]
  deathYear=[]
  primaryProfession=[]
  knownForTitles=[]

  df=pd.read_table("index.tsv")

  df.to_csv('index.csv' ,encoding='utf-8')
  out=pd.read_csv('index.csv',encoding='utf-8')
  celda=int(out.shape[0])



  for celdas in range(celda):
          
      if out.iloc[celdas,1].find('ö') != -1:
          nconst.append(out.iloc[celdas,1].replace('ö','o'))
      elif out.iloc[celdas,1].find('â') != -1:
          nconst.append(out.iloc[celdas,1].replace("â","a"))
      elif out.iloc[celdas,1].find('ñ') != -1:
          nconst.append(out.iloc[celdas,1].replace("ñ","n"))
      elif out.iloc[celdas,1].find('ç') != -1:
          nconst.append(out.iloc[celdas,1].replace("ç","c"))
      elif out.iloc[celdas,1].find('á') != -1:
          nconst.append(out.iloc[celdas,1].replace("á","a"))
      elif out.iloc[celdas,1].find('ä') != -1:
          nconst.append(out.iloc[celdas,1].replace("ä","a"))

      else:
            nconst.append(out.iloc[celdas,1])
  



      
      if out.iloc[celdas,2].find('ö') != -1:
        primaryname.append(out.iloc[celdas,2].replace('ö','o'))
      elif out.iloc[celdas,2].find('â') != -1:
        primaryname.append(out.iloc[celdas,2].replace("â","a"))
      elif out.iloc[celdas,2].find('ã') != -1:
        primaryname.append(out.iloc[celdas,2].replace("ã","a"))
      elif out.iloc[celdas,2].find('ñ') != -1:
        primaryname.append(out.iloc[celdas,2].replace("ñ","n"))
      elif out.iloc[celdas,2].find('ç') != -1:
       primaryname.append(out.iloc[celdas,2].replace("ç","c"))
      elif out.iloc[celdas,2].find('á') != -1:
        primaryname.append(out.iloc[celdas,2].replace("á","a"))
      elif out.iloc[celdas,2].find('ä') != -1:
        primaryname.append(out.iloc[celdas,2].replace("ä","a"))
      elif out.iloc[celdas,2].find('û') != -1:
        primaryname.append(out.iloc[celdas,2].replace("û","u"))
      elif out.iloc[celdas,2].find('ü') != -1:
        primaryname.append(out.iloc[celdas,2].replace("ü","u"))
      elif out.iloc[celdas,2].find('ô') != -1:
        primaryname.append(out.iloc[celdas,2].replace("ô","o"))
      elif out.iloc[celdas,2].find('å') != -1:
        primaryname.append(out.iloc[celdas,2].replace(" å","a"))

      elif out.iloc[celdas,2].find("Ô") != -1:
        primaryname.append(out.iloc[celdas,2].replace("Ô","o"))
      elif out.iloc[celdas,2].find("Ö") != -1:
        primaryname.append(out.iloc[celdas,2].replace("Ö","o"))
        
        


      else:
        primaryname.append(out.iloc[celdas,2])



      if out.iloc[celdas,3].find('ö') != -1:
        birthYear.append(out.iloc[celdas,3].replace('ö','o'))
      elif out.iloc[celdas,3].find('â') != -1:
        birthYear.append(out.iloc[celdas,3].replace("â","a"))
      elif out.iloc[celdas,3].find('ñ') != -1:
        birthYear.append(out.iloc[celdas,3].replace("ñ","n"))
      elif out.iloc[celdas,3].find('ç') != -1:
        birthYear.append(out.iloc[celdas,3].replace("ç","c"))
      elif out.iloc[celdas,3].find('á') != -1:
        birthYear.append(out.iloc[celdas,3].replace("á","a"))
      elif out.iloc[celdas,3].find('ä')!= -1:
       birthYear.append(out.iloc[celdas,3].replace("ä","a"))

      else:
       birthYear.append(out.iloc[celdas,3])




    
      if out.iloc[celdas,4].find('ö') != -1:
        deathYear.append(out.iloc[celdas,4].replace('ö','o'))
      elif out.iloc[celdas,4].find('â') != -1:
        deathYear.append(out.iloc[celdas,4].replace("â","a"))
      elif out.iloc[celdas,4].find('ñ') != -1:
        deathYear.append(out.iloc[celdas,4].replace("ñ","n"))
      elif out.iloc[celdas,4].find('ç') != -1:
        deathYear.append(out.iloc[celdas,4].replace("ç","c"))
      elif out.iloc[celdas,4].find('á') != -1:
        deathYear.append(out.iloc[celdas,4].replace("á","a"))
      elif out.iloc[celdas,4].find('ä') != -1:
       deathYear.append(out.iloc[celdas,4].replace("ä","a"))

      else:
          deathYear.append(out.iloc[celdas,4])
          primaryProfession.append(out.iloc[celdas,5])
          knownForTitles.append(out.iloc[celdas,6])





  dtnconst=nconst
  dtprimaryname=primaryname
  dtbirthYear=birthYear
  dtdeathYear=deathYear
  dtprimaryProfession=primaryProfession
  dtknownForTitles=knownForTitles


  resultado = pd.DataFrame({
                        'dtnconst':nconst,
                        'dtprimaryname':primaryname,
                        'dtbirthYear':birthYear,
                        'dtdeathYear':deathYear,
                        'dtprimaryProfession':primaryProfession,
                        'dtknownForTitles':knownForTitles
                        })


  resultado.to_csv('salida.csv',encoding='UTF-8')
  
  return resultado



    
ejercicio(r)