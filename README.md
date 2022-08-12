# Babylon
Microservices using mutliple languages (as with Babylon's tower) for a fake e-commerce

## Contents

1. [Motivation](#motivation)
1. [Architecture](#architecture)
    1. [Microservices pattern](#microservices-pattern)
    1. [Monorepo vs Multirepo](#monorepo-vs-multirepo)
1. [Idea](#idea)
1. [Microservices](#microservices)
    1. [Python (Django and Flask)](#python-django-and-flask)
    1. [Ruby (on Rails)](#ruby-on-rails)
    1. [PHP (Laravel)](#php-laravel)
    1. [Java (SpringBoot)](#java-springboot)
    1. [Golang (Gin-gonic)](#golang-gin-gonic)
    1. [Javascript (Typescript)](#javascript-typescript)
    1. [C++](#c)
    1. [Rust](#rust)
    1. [C#.NET](#cnet)
1. [Credits](#credits)

## Motivation

I wanted to try out the microservices architecture, and, while doing so, try out and learni different languages and stacks. I wanted to create a project with different services and different languages, not because of maintainability, because it would obviously be something out of hand. But as of a challenge rather.

I've chosed babylon to represent the amount of languages, and I also liked the idea of it's ambicousness, because it could, well likely, be the downfall of this project.

## Architecture

An explanation about my choices and my reasoning.

### Microservices pattern

As aforementioned, I wanted to try out microservices for the longest, well, that may have been an exaggeration, but they do seem intresting, and something I've never tried, but that makes a ton of sense.

Microservices are now everywhere (almost, so to speak) they're really popular. Not saying it's a good or bad thing. It has it's own pros and cons, clearly stated at the official guide. Not everyone, nor every project fits the microservices pattern, or rather, the pattern doesn't firt the project's or team's requirements and/or needs, which is just fine.

### Monorepo vs Multirepo

A long question, I've chosen, or at least, it is my idea for now, multirepo. I initially thought of monorepo, because of easeness while looking for the project and exploring it. And it's not something impossible, turborepo it's out there and working just fine, and other solutions made for microservices hosted on a monorepo.

What made me say, let's do multirepo! The fact that, each service should be independant of the other services as much as posible, and they will all have different languages. So, what would be the purpose having a single repository, what could be the scalability of a monorepo (considering I'm not Google nor this is a lifelong project). I'd like to abstract each service with it's own repository, and one repo seems risky to me.

Also, reading different opinions (which there are, and not a clear answer, if something, multirepo seems a little bit more liked), having one repo may contribute to "bad practices" such as sharing common elements. [Point of reference](https://stackoverflow.com/questions/54582640/what-would-be-the-standard-and-better-approach-of-the-git-repository-structure-f).

## Idea

I'm going to create the least original idea for microservices, simply, because the product for this project it's not going to be it's strongest point, and, I'm learning, I want a starting ground I can base my suppositions around.

That being said, what am I going to do? An E-Commerce!! For real. Sparked by IBM's introduction video to microservices and it's pre-defined structure it provides as an example.

[
    ![What are Microservices? by IBM Technology](https://img.youtube.com/vi/CdBtNQZH8a4/0.jpg)\
    _What are Microservices? by IBM Technology_
](https://www.youtube.com/watch?v=CdBtNQZH8a4)

## Microservices

The links and brief explanation of each microservice

### Python (Django and Flask)

Link to repository...

### Ruby (on Rails)

Link to repository...

### PHP (Laravel)

Link to repository...

### Java (SpringBoot)

Link to repository...

### Golang (Gin-gonic)

Link to repository...

### Javascript (Typescript)

Link to repository...

### C++

Link to repository...

### Rust

Link to repository...

### C#.NET

Link to repository...

## Credits

To [microservices.io](https://microservices.io) and [Chris Richardson](https://github.com/cer)\
And to [IBM's Technology YouTube channel](https://www.youtube.com/channel/UCKWaEZ-_VweaEx1j62do_vQ)