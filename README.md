# BioPaper Fetcher CLI

A lightweight CLI tool to search and retrieve biomedical articles using [Europe PMC REST API](https://europepmc.org/RestfulWebService).

```mermaid
flowchart TD
    A[Start CLI] --> B{CLI Flags Provided?}
    B -- Yes --> C[Parse Args-  e.g: -q, -l, --open-acces]
    B -- No --> D[Display Interactive Menu]
    D --> E[Get User Input]
    C --> F[Send GET Request to Europe PMC API]
    E --> F
    F --> G{Response Status 200?}
    G -- No --> H[Display API Error Message]
    G -- Yes --> I[Parse JSON & Prepare Data]
    I --> J[Display Prepared Terminal Output]
    J --> K{Output File Specified?}
    K -- Yes --> L[Save Articles to JSON File]
    K -- No --> M[End]
    L --> M
    
```

## Usage

```bash
# Flag mode (Direct search)
python main.py -q "CRISPR" -l 3 --open-access

# Interactive mode (Interactive input)
python main.py
```

> **[!] Note:** This is an initial prototype (v0.1.0). Additional features and enhancements are actively planned.