# What is this?

This is the source code to the docker image at https://hub.docker.com/r/kognate/stemmer/

This docker image is setup to be used as an OpenWhisk action and will stem and lemmatize 
an english query sent to it.  

`$ wsk action create stemmer --docker kognate/stemmer`

Now you have an action that can be called like this:

`$ wsk -v action invoke stemmer --blocking --result -p query "the quickest foxes"`

You can also expose it via the experimental api-connect like this:

`$ wsk api-experimental create /example /stemmer get stemmer`
