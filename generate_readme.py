#! python3
from os import listdir
from os.path import join
bannerImg = "https://f.thumbs.redditmedia.com/_23zdeL5L1OqQyIw.png"
bannerUrl = "https://www.reddit.com/r/dailyprogrammer/"
text = []
text.append('[![dailyprogrammer banner](%s "r/dailyprogrammer")](%s)' %
            (bannerImg, bannerUrl))

problemPath = join(".", "problems")
githubPath = "/problems/"
problems = tuple(sorted(listdir(path=problemPath), reverse=True))
for path in problems:
    pText = []
    date, name = path.rstrip(".py").split(" ", 1)
    relPath = githubPath + path.replace(" ", "%20").replace("#", "%23")
    with open(join(problemPath, path)) as f:
        f.readline()
        url = f.readline().lstrip("# ")
    pText.append('  * [%s](%s "Problem post at reddit")' % (date, url))
    pText.append("[%s](%s)" % (name, relPath))
    text.append(" - ".join(pText))
text.append("""#### License
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.""")
with open("README.md", "w") as f:
    f.write("\n\n".join(text))
