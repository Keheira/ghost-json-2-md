import json
import pypandoc
import io
import os
import sys

def main():
   
   if len(sys.argv) < 2:
      print("Error: Please provide a file path.")
      return
   
   if len(sys.argv) < 3:
      print("Error: Please provide an output folder.")
      return

   filePath = sys.argv[1]
   outPath = sys.argv[2]

   ProcessJson(filePath, outPath)

   print(f"Finished, check {outPath} folder")

def ProcessJson(inputFile, outputPath):
   # open json file
   with io.open(inputFile, encoding='utf-8') as read_file:
      data = json.load(read_file)
   
   # Create output folder
   folderpath = outputPath
   if not os.path.exists(folderpath):
      os.makedirs(folderpath)
   
   for entry in data["db"][0]["data"]["posts"]:
      title = entry['title']

      featureImageTemp = entry['feature_image']
      if featureImageTemp is not None and featureImageTemp[0] == "/":
         featureImage = featureImageTemp[8:]
      else:
         featureImage = featureImageTemp
      
      htmlText = entry['html']
      creationDate = entry['published_at'][:-14]
      updateDate = entry['updated_at'][:-14]
      publishDate = entry['published_at'][:-14]
      if entry['status'] == 'published':
         isPublished = True
      else:
         isPublished = False
      
      # pyndoc for html to md
      mdText = pypandoc.convert_text(htmlText, 'md', 'html')
      
      filename = title + ".md"
      newfile = io.open(folderpath  +  "/" + filename , mode="a", encoding="utf-8")
      
      newfile.write("---\n")
      newfile.write(f"tags: \n - fromGhost\n")
      newfile.write(f"publish: {isPublished}\n")
      newfile.write(f"updated: {updateDate}\n")
      if isPublished:
         newfile.write(f"created: {publishDate}\n")
      else:
         newfile.write(f"created: {creationDate}\n")
      newfile.write("---\n")
      if featureImageTemp is not None:
         newfile.write(f"![featured image]({featureImage})\n\n")
      newfile.write(mdText)
      newfile.close()

   tagFile = io.open(folderpath  +  "/tags.txt" , mode="a", encoding="utf-8")
   for tag in data["db"][0]["data"]["tags"]:
      tagFile.write(f"- {tag['name']}\n")
      
   tagFile.close()


if __name__ == "__main__":
   main()