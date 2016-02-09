# img_getter
Gets images using Bing Img Search

To get this to work, you'll need a file config.py with your Bing API key in it (get yours for free here - http://datamarket.azure.com/dataset/bing/search), as well as a .csv file with a column called 'words' in it.

Example of use:

```python
import get_images

get_images.getWords('word_list.csv', 'word_dir')

```
