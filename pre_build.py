def on_pre_build(**kwargs):
    markdown.extensions.toc.slugify = slugify


import re
import unicodedata
import markdown

def slugify(value, separator, unicode=False):
    """ Slugify a string, to make it URL friendly. """
    findList = re.findall(r'\{#(.*?)\}', value)
    if len(findList) > 0:
        value = findList[0]
    if not unicode:
        # Replace Extended Latin characters with ASCII, i.e. `žlutý` => `zluty`
        value = unicodedata.normalize('NFKD', value)
        value = value.encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[{}\s]+'.format(separator), separator, value)



def on_post_page(output, **kwargs):
    return re.sub(r'\{#(.*?)\}', '', output)