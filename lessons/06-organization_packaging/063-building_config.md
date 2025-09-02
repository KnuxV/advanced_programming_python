
### Installing Your Package Locally

#### Editable Installation (Development Mode)
This creates a link to your package, so changes are reflected immediately:
```bash
pip install -e .
```

#### Regular Installation
```bash
pip install .
```

### Building Your Package

First, install build tools:
```bash
pip install build
```

Then build your package:
```bash
python -m build
```

This creates two files in the `dist/` directory:
- `.tar.gz` - Source distribution
- `.whl` - Wheel (binary) distribution

