# Stardeus Translations

The translations files are CSV exported from Google Sheets. You can find the original English sheet for Core mod over here:

https://docs.google.com/spreadsheets/d/1iiaORk6Ma5c2DpijK3oFs08fdk9PAe7QsCoiiBzdEUU/edit?usp=sharing

First line of the translation file should be the header, and it is going to be ignored by translations system.

Please note that anything within curly braces {} is for variables
and their formatting.

If you are creating a new mod that introduces texts in UI or elsewhere, you must add newly created keys to your mod's Translation folder's English.csv.

If a translation doesn't appear, you have likely forgotten the trailing comma (if comment is blank). CSV format is:
`key,translation,version,comment`