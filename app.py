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

      featureImage = entry['feature_image']
      
      htmlText = entry['html']
      creationDate = entry['published_at'][:-14]
      updateDate = entry['updated_at'][:-14]
      publishDate = entry['published_at'][:-14]
      slug = entry['slug']
      description = entry['custom_excerpt']
      if entry['status'] == 'published':
         isPublished = True
      else:
         isPublished = False

      tags = tagsForPost(
         data["db"][0]["data"]['posts_tags'],
         entry['id'],
         data["db"][0]["data"]["tags"]
      )
      
      # pyndoc for html to md
      mdText = pypandoc.convert_text(source=htmlText, to='md', format='html')
      
      filename = title + ".md"
      newfile = io.open(folderpath  +  "/" + filename , mode="a", encoding="utf-8")
      
      newfile.write("---\n")
      if not tags:
         newfile.write(f"tags: \n")
      else:
         newfile.write(f"tags:")
         for tag in tags:
            newfile.write(f"\n{tag}")
      newfile.write(f"publish: {isPublished}\n")
      newfile.write(f"updated: {updateDate}\n")
      if isPublished:
         newfile.write(f"created: {publishDate}\n")
      else:
         newfile.write(f"created: {creationDate}\n")
      newfile.write(f"permalink: {slug}\n")
      newfile.write(f"description: {description}\n")
      newfile.write("---\n")
      if featureImage is not None:
         newfile.write(f"![featured image]({featureImage})\n\n")
      newfile.write(mdText)
      newfile.close()

def tagsForPost(postTags, currentPostId, tags):
   post_tag = []
   for post in postTags:
      if post['post_id'] == currentPostId:
         for tag in tags:
            if tag['id'] == post['tag_id']:
               post_tag.append(f"- {tag['name']}\n")
   return post_tag

if __name__ == "__main__":
   main()