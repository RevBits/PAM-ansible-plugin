from distutils.core import setup

setup(
  name = 'revbits_ansible',
  packages = ['revbits_ansible'],
  package_dir={'': 'pam'},
  version = '1.3',
  license='MIT',
  description = 'The PAM Secret Server Python SDK',
  author = 'RevBits',
  author_email = 'info@revbits.com',
  keywords = ['PAM', 'Secret', 'Security', 'RevBits'],
  install_requires=[
        'requests>=2.22.0'
        'python-dotenv'
        'flit'
        'pycryptodome'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of package
    'Intended Audience :: Developers',
    'Topic :: Security',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
