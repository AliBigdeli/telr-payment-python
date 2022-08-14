from setuptools import setup, find_packages


setup(
    name='telr_payment',
    version='0.1',
    license='MIT',
    author="Ali Bigdeli",
    author_email='bigdeli.ali3@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/alibigdeli/telr-payment',
    keywords=['telr','payment','payment gateway','telr payment'],
    install_requires=[
          'requests',
      ],
    classifiers=[
        'Development Status :: 1 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',   
        'Environment :: Console',
        'Environment :: Web Environment',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',        
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],

)
