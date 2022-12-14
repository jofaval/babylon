# Babylon
Microservices using mutliple languages (as with Babylon's tower) for a fake e-commerce

It's managed with a Github Project (beta) to keep track of all of the repositories, [[Microservices] Babylon E-Commerce](https://github.com/users/jofaval/projects/5).

## Contents

1. [Motivation](#motivation)
1. [Microservices](#microservices)
1. [Microfrontends](#microfrontends)
1. [Cloning the repository](#cloning-the-repository)
1. [Architecture](#architecture)
    1. [Microservices pattern](#microservices-pattern)
    1. [Monorepo vs Multirepo](#monorepo-vs-multirepo)
1. [Idea](#idea)
1. [Credits](#credits)

## Motivation
[⬆ Return to the contents](#contents)

I wanted to try out the microservices architecture, and, while doing so, try out and learni different languages and stacks. I wanted to create a project with different services and different languages, not because of maintainability, because it would obviously be something out of hand. But as of a challenge rather.

I've chosed babylon to represent the amount of languages, and I also liked the idea of it's ambicousness, because it could, well likely, be the downfall of this project.

## Microservices
[⬆ Return to the contents](#contents)

The links and brief explanation of each microservice

- **[API Gateway](./babylon-api-gateway-service/)** - Go(lang) and Gingonic, maybe Janus.
- **[API Gateway UI](./babylon-api-gateway-ui-service/)** - Go(lang) and Gingonic, maybe Janus.
- **[Carts](https://github.com/jofaval/babylon-carts-service/)** - PHP (Laravel)
- **[Catalog](https://github.com/jofaval/babylon-catalog-service/)** - _To be defined..._
- **[Comments](https://github.com/jofaval/babylon-comments-service/)** - _To be defined..._
- **[Customers](https://github.com/jofaval/babylon-customers-service/)** - _To be defined..._
- **[Inventory](https://github.com/jofaval/babylon-inventory-service/)** - _To be defined..._
- **[Orders](https://github.com/jofaval/babylon-orders-service/)** - _To be defined..._
- **[Payments](https://github.com/jofaval/babylon-payments-service/)** - _To be defined..._
- **[Recommendations](https://github.com/jofaval/babylon-recommendations-service/)** - Python + Tensorflow
- **[Reporting](https://github.com/jofaval/babylon-reporting-services/)** - _To be defined..._
- **[Reviews](https://github.com/jofaval/babylon-reviews-service/)** - _To be defined..._

## Microfrontends
[⬆ Return to the contents](#contents)

They're detailed in it's own repository/submodule, so check it out without any problem for the most up-to-date info.

- **[UI](https://github.com/jofaval/babylon-ui/)** - TypeScript, JavaScript, React (Remix) and Astro

## Cloning the repository
[⬆ Return to the contents](#contents)

You'll have to clone the repository, but this one, it is a special one. It uses submodules, which are links to other repositories, sort of.

For Git >= 2.13:

```bash
git clone --recurse-submodules -j8 git://github.com/jofaval/babylon.git
cd babylon
```

_`-j8` will allow to download up to 8 submodules at once._

For older Git versions compatibility, this would be the commands:

```bash
git clone git://github.com/jofaval/babylon.git
cd babylon
git submodule update --init --recursive
```

Any specification needed for a given service will be detailed at that specific service.

## Architecture
[⬆ Return to the contents](#contents)

An explanation about my choices and my reasoning.

### Microservices pattern
[⬆ Return to the contents](#contents)

As aforementioned, I wanted to try out microservices for the longest, well, that may have been an exaggeration, but they do seem intresting, and something I've never tried, but that makes a ton of sense.

Microservices are now everywhere (almost, so to speak) they're really popular. Not saying it's a good or bad thing. It has it's own pros and cons, clearly stated at the official guide. Not everyone, nor every project fits the microservices pattern, or rather, the pattern doesn't firt the project's or team's requirements and/or needs, which is just fine.

### Monorepo vs Multirepo
[⬆ Return to the contents](#contents)

A long question, I've chosen, or at least, it is my idea for now, multirepo. I initially thought of monorepo, because of easeness while looking for the project and exploring it. And it's not something impossible, turborepo it's out there and working just fine, and other solutions made for microservices hosted on a monorepo.

What made me say, let's do multirepo! The fact that, each service should be independant of the other services as much as posible, and they will all have different languages. So, what would be the purpose having a single repository, what could be the scalability of a monorepo (considering I'm not Google nor this is a lifelong project). I'd like to abstract each service with it's own repository, and one repo seems risky to me.

Also, reading different opinions (which there are, and not a clear answer, if something, multirepo seems a little bit more liked), having one repo may contribute to "bad practices" such as sharing common elements. [Point of reference](https://stackoverflow.com/questions/54582640/what-would-be-the-standard-and-better-approach-of-the-git-repository-structure-f).

## Idea
[⬆ Return to the contents](#contents)

I'm going to create the least original idea for microservices, simply, because the product for this project it's not going to be it's strongest point, and, I'm learning, I want a starting ground I can base my suppositions around.

That being said, what am I going to do? An E-Commerce!! For real. Sparked by IBM's introduction video to microservices and it's pre-defined structure it provides as an example.

[
    ![What are Microservices? by IBM Technology](https://img.youtube.com/vi/CdBtNQZH8a4/0.jpg)\
    _What are Microservices? by IBM Technology_
](https://www.youtube.com/watch?v=CdBtNQZH8a4)

## Credits
[⬆ Return to the contents](#contents)

To [microservices.io](https://microservices.io) and [Chris Richardson](https://github.com/cer)\
And to [IBM's Technology YouTube channel](https://www.youtube.com/channel/UCKWaEZ-_VweaEx1j62do_vQ)