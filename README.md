[![Netlify Status](https://api.netlify.com/api/v1/badges/25d1f9af-bfec-4f6f-b521-28f17722360a/deploy-status)](https://app.netlify.com/sites/ieeecomputersociety/deploys)

# IEEE Computer Society UnB Site

This is the IEEE Computer Society UnB site, it's a simple site that uses a simple
custom static page generator and [Jinja 2](http://jinja.palletsprojects.com/en/2.10.x/),
a templating tool, for News and Coding Dojo articles.

While it's main pages are mostly static, we have a few sections that are constantly
being updated with new information. Such sections are the Dojo and the News sections.
We use a markdown file to generate new posts in each category.

## Before you start

If you're going to help this site's development, we highly recommend you read the
following [article](https://markentier.tech/posts/2018/04/progressive-web-app/),
it covers the basic stuff and most of the best practices for maintaining a fast and
accessible site. So, READ IT.

If you're just using the repo for your personal project, we also advise you to
read the article, since it's important to have a fast site that works perfectly,
also it's good to understand a bit more about site performance.

## Setting up

Assuming you already created and activated a virtual environment 

```shell script
python generator.py
```

## Merging changes

```
For a Merge Request to be accepted in develop, a branch must have all linters running with no problem.

To be accepted in staging, it must be approved by @alexandrebarbaruiva

To be accepted in master, it must be approved by @tapumar and @anna_thais

```

# References

https://mxb.dev/blog/how-to-turn-your-website-into-a-pwa/
https://developers.google.com/web/fundamentals/codelabs/your-first-pwapp/?hl=pt-br
https://serviceworke.rs/
https://codelabs.developers.google.com/codelabs/migrate-to-progressive-web-apps/index.html#0
https://www.reddit.com/r/webdev/comments/cwhaop/do_you_really_develop_mobile_first/
https://www.pwabuilder.com/
http://www.html-tidy.org/
https://imagemagick.org/index.php
