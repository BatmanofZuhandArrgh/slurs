# Slur Collection Repository  

This repository contains a manually curated collection of slurs sourced from Wikipedia. The focus is on slurs that are **unambiguously derogatory**, meaning they are primarily used as insults and cannot be reasonably interpreted as neutral or context-dependent terms.  

## **Missing Slurs**  
Examples of slurs which are excluded, due to them being also possibly non-slur based on context:
- **Ape** – Black people  
- **Brownie** – South Asian or Southeast Asian people  
- **Pajeet, Pocahontas, Uncle Tom** – Real names of characters but often used derogatorily
- etc...  

## **Sources**  
Slurs have been collected from various Wikipedia pages, focusing on categories where words are primarily used as insults:  

- **Ethnic Slurs (U.S.)** – [Wikipedia: List of ethnic slurs](https://en.wikipedia.org/wiki/List_of_ethnic_slurs)
    Note: Chosen due to the popular social media sites being U.S.-centric 
- **Religious Slurs** – [Wikipedia: List of religious slurs](https://en.wikipedia.org/wiki/List_of_religious_slurs) 
    Note: **Excluded**, since I do not have the knowledge to pick and choose
- **Disability-Related Slurs** – [Wikipedia: List of disability-related terms with negative connotations](https://en.wikipedia.org/wiki/List_of_disability-related_terms_with_negative_connotations)    
- **LGBTQ+ Slurs** – [Wikipedia: LGBTQ-related slurs](https://en.wikipedia.org/wiki/Category:LGBTQ-related_slurs)  
  - Includes terms that, in my personal opinion, have **not** been successfully reclaimed by the LGBTQ+ community and are still used as insults.  
- **Gender-Related Slurs** – [Wikipedia: Sex- and gender-related slurs](https://en.wikipedia.org/wiki/Category:Sex-_and_gender-related_slurs)  



# Word Obfuscation Script  
This repository also includes a **`convert.py`** script, which modifies words by replacing **1-3 characters** using **visually similar alternatives**.  

This script is useful for:  
- **Testing moderation systems** to ensure they can catch altered slurs.  
- **Generate toxic data** used for text detoxification AI training.  

### **How It Works**  
- Reads the **YAML file** containing **character substitutions** (e.g., "a" → "@", "e" → "3"), generated by GPT4o.  
- Used  *vowel_prob* to choose randomly indices of characters to modify, as vowels are more commonly altered in online evasion tactics.  
- Randomly modifies characters in a word.  
- It also support pluralize, repeats or insert split characters in the word.

### **Example Usage**  
Edit the parameters in `convert.py`, then run:

```
python convert.py
```


## **Contributing**  
If you know of any additional slurs or online evasion tactics that meet the inclusion criteria, feel free to submit an issue or pull request.  

## **Disclaimer**  
This repository is for **educational and reference purposes only**. It does **not** endorse or promote the use of any of these terms or code for malicious purposes. The goal is to document language used in a derogatory manner to aid in awareness, research, and content moderation efforts.   