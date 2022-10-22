# Scrapper for La Gaceta Newspaper
La Gaceta is a newspaper very popular in the Cotopaxi province in the Ecuador Country.

Link to La Gaceta newspaper: https://lagaceta.com.ec/

All the scraping process followed the rules of the robots.txt file.

----

**Table of Contents**

* **news.py** is the file that allows doing the scrapping in the website.


----

### Outcomes 

- A folder with the for each date that "news.py" is executed.

- The folder with the date has the news published and are currently public. 

- Each notice is saved like a .txt file with and the name is the title.
 
----

                
### FlowChart of the Scrapping
---
```mermaid 
  graph TD
    A[Access to the index of the website] --> B[Verify the website is online]
    B --> C[Extract the links of the notices]
    C --> D[Save links in a list]
    D --> E[Loop over the list]
    E --> F[Verify each notice is online]
    F --> G[Extract title and paragraphs]
    G --> H[Create a folder with the date]
    H --> K[Create files for each notices and save like txt]


```

### Contacts:
---
- [Twitter](https://twitter.com/sarasti_seb)
- [LinkedIn](https://linkedin.com/in/sebastiansarasti)
- [ResearchGate](https://www.researchgate.net/profile/Sebastian-Sarasti-2)
