# Scrapper for La Gaceta Newspaper
La Gaceta is a newspaper very popular in the Cotopaxi province in the Ecuador Country.

Link to La Gaceta newspaper: https://lagaceta.com.ec/

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
    C --> D[Extract the links of the notices]
    D --> E[Save links in a list]
    E --> F[Loop over the list]
    F --> G[Verify each notice is online]
    G --> H[Extract title and paragraphs]
    H --> K[Create a folder with the date]
    K --> L[Create files for each notices and save like txt]


```

### Contacts:
---
- [Twitter](https://twitter.com/sarasti_seb)
- [LinkedIn](https://linkedin.com/in/sebastiansarasti)
- [ResearchGate](https://www.researchgate.net/profile/Sebastian-Sarasti-2)
