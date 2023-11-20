---
layout: single
permalink: /tutorials/create-development-environment.html
classes: wide
title: "Create a Python development environment "
excerpt: "More here"
header:
  overlay_color: "#666"
  overlay_filter: 0.6
author_profile: false
---

{% include packaging-toc %}

1. how to do it with venv

### Creating a PyOS-Dev Environment Using venv

1. **Open Terminal or Command Prompt:**

   - Open your terminal or command prompt.

2. **Navigate to the Project Directory:**

   ```bash
   cd path/to/your/project-directory
   ```

3. **Create a Virtual Environment:**

   ```bash
   python -m venv pyos-dev
   ```

4. **Activate the Virtual Environment:**

   - **On Windows:**

   ```bash
   pyos-dev\Scripts\activate
   ```

   - **On macOS/Linux:**

   ```bash
   source pyos-dev/bin/activate
   ```

5. **Install/Manage Dependencies:**

   ```bash
   pip install package_name
   ```

6. **Work on Your Project:**

7. **Deactivate the Virtual Environment:**
   ```bash
   deactivate
   ```

### Additional Notes:

- Remember to reactivate the environment each time you want to work on your project.
- To delete the virtual environment, delete the `pyos-dev` folder.

2. how to do it with conda forge

### Creating a PyOS-Dev Environment Using Conda

1. **Create an Environment File (`env.yml`):**

   - Use a text editor to create a file named `env.yml` and specify the required packages in the YAML format. For instance:

   ```yaml
   name: pyos-dev
   channels:
     - defaults
   dependencies:
     - python=3.8
     - package_name1
     - package_name2
     # Add other necessary packages
   ```

2. **Create the Conda Environment from the Environment File:**

   - Open your terminal or command prompt.

   ```bash
   conda env create -f env.yml
   ```

   This command will read the `env.yml` file and create a Conda environment named `pyos-dev` with the specified packages.

3. **Activate the Conda Environment:**

   - Once the environment is created, activate it.
   - **On Windows:**

   ```bash
   conda activate pyos-dev
   ```

   - **On macOS/Linux:**

   ```bash
   source activate pyos-dev
   ```

4. **Work on Your Project:**
   - You're now working in the `pyos-dev` Conda environment.

### Additional Notes:

- Remember to activate the environment each time you want to work on your project.
- To deactivate the environment, use `conda deactivate`.
- To delete the environment, you can use `conda env remove -n pyos-dev`.
