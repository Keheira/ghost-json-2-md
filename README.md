# Ghost to JSON to MD

Used this to convert my json file from ghost cms to markdown to use in obsidian.

** One big assuption I'll be making here is that you have a folder called `/content/images/` already in obsidian. Any local photos will look for items there **

## How to run
`python3 app.py <input_file> <output_folder>`

There will be 1 file types created in the output folder.

### post files (<post_title>.md)
```
---
tags:
  - <post_tag>
publish: <true_or_false>
updated: <update_date> (YYYY-MM-DD)
created: <publish_date_or_created_date> (YYYY-MM-DD)
---
<featured_image>

<text_from_blog_post>
```
