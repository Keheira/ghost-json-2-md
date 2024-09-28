# Ghost to JSON to MD

Used this to convert my json file from ghost cms to markdown to use in obsidian.

** One big assuption I'll be making here is that you have a folder called /images already in obsidian. Any local photos will look for items there **

There will be 2 file types created in the output folder.

### post files
```
---
tags:
  - fromGhost
publish: true
updated: <YYYY-MM-DD>
created: <YYYY-MM-DD>
---
<featured_image>

<text_from_blog_post>
```
### tag file
```
- tag1
- tag2
```
