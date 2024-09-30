# Grabify Domains

Welcome to the Grabify Domains repository! This repository aims to provide an up-to-date list of all known Grabify domains, allowing users to easily blacklist them and protect their privacy.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)

## Introduction

Grabify is a service used to create trackable links that can log IP addresses and other information about the visitors. While this can be used for legitimate purposes, it is often exploited for malicious intent. This repository aims to maintain a comprehensive list of Grabify domains to help users block these domains and protect their privacy.

## Usage

To use as blacklist:

1. **Download the List:**
   - Clone the repository or download the `domain-list` file directly.

   ```bash
   git clone https://github.com/mayzelf/grabify-domains.git
   ```

2. **Import the List:**
   - Import the `domain-list` file into your firewall, ad blocker, or any other tool you use to manage blacklists.

3. **Regular Updates:**
   - Ensure you regularly update the list to stay protected against new Grabify domains.

### Skript

#### Installation

1. Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Install the BeautifulSoup library by running the following command:

```bash
pip install beautifulsoup4
```

#### Usage

1. **Prepare the input file:**
   - Ensure you have an input file named `dropdown.txt` in the same directory as the script. This file should contain the HTML content to be processed.

2. **Run the script:**
   - Execute the script using Python:

   ```bash
   python parser.py
   ```

3. **Output:**
   - The script will create an output file named `domains.txt` in the same directory. This file will contain the extracted text from the 'a' tags and their nested 'small' tags, each on a new line.

An example of how the input should look can be found inside `dropdown.txt`.

## Contributing

Contributions are welcome! If you know of any Grabify domains that are not listed here, please contribute by following these steps:

1. **Fork the Repository:**
   - Click the "Fork" button on the top right corner of this page.

2. **Clone the Forked Repository:**
   - Make sure to replace 'yourusername' with your username.
   ```bash
   git clone https://github.com/yourusername/grabify-domains.git
   ```

3. **Add the New Domain:**
   - Open the `domain-list` file and add the new domain(s) at the end of the list.

4. **Commit Your Changes:**

   ```bash
   git commit -am 'Add new Grabify domain'
   ```

5. **Push to Your Forked Repository:**

   ```bash
   git push origin main
   ```

6. **Create a Pull Request:**
   - Go to the original repository and create a pull request to merge your changes.

## Contact

If you have any questions, suggestions, or issues, please feel free to contact me:

- GitHub: [mayzelf](https://github.com/mayzelf)
- Discord: mayzelf
- Website: [mayzelf.xyz]https://mayzelf.xyz/contact
