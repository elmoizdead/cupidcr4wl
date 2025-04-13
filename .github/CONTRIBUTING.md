<div align="center">
  
# 🌟 Thank you for taking the time contribute to cupidcr4wl 🌟

</div>

>A note on contributing, DO NOT submit a platform that is involved in hosting illegal activity, it will be ignored and removed!

## If you are interested in submiting a platform to the cupidcr4wl search list, there are two ways to do so:

**The easy way:**

Please submit your contribution in the [issues section](https://github.com/OSINTI4L/cupidcr4wl/issues), there you will find issue templates to enter the platform information. If you are reporting a false positive/negative, this can be done here as well.

**The hard way:**

 Submit a pull-request to the [websites.json](https://github.com/OSINTI4L/cupidcr4wl/blob/main/websites.json) file or [phonenumbers.json](https://github.com/OSINTI4L/cupidcr4wl/blob/main/phonenumbers.json) file.

The format will require the following:

```
        },
	"Platform Name": {
            "url": "https://url/path/to/user/profile/{username or phone number}",
            "check_text": [
                "html snippets from profile page"
            ],
              "not_found_text": [
                "html snippets from a non-profile page"
            ],
            "category": "Relevant category"
```
The following categories are currently used by cupidcr4wl:

- Payment and Gifting
- Social
- Dating and hook-up
- Fetish
- Adult video and photo
- Camming
- Escort

If contributing via pull request, please read the [accuracy implementations]() section in the documentation to understand how to choose HTML snippets for `check_text` and `not_found_text` correctly and accurately.
