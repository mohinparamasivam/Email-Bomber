# Email Bomber

Spam emails to a single email address

<b> Use this tool for educational purpose only !! </b>

# Installation

Download the tool:
```bash
git clone https://github.com/mohinparamasivam/Email-Bomber.git
```
OR
```bash
wget https://github.com/mohinparamasivam/Email-Bomber/archive/refs/heads/master.zip
unzip master.zip
rm masper.zip
```

## Setup Gmail account

> The instructions are based on [this google support article](https://support.google.com/accounts/answer/185833)

#### Step 1: Enable 2FA
Go to [this link](https://myaccount.google.com/signinoptions/two-step-verification) and follow the steps to enable 2FA

#### Step 2: Generate an App Password
Go to [this link](https://myaccount.google.com/apppasswords), in select device click on other and type the name you want

<image src="media/1.png">
<image src="media/2.png">

Then click on generate button
<image src="media/3.png">

And copy this password (without spaces)
<image src="media/4.png">

In this case, in attacker email password i would have to put `swyujgqqgnlwdqqv`

#### Step 3: Enjoy!

> Remember: 2FA must be kept enabled.<br>
> If you disable, it the wont work.

# Usage

Run it with Python 3: 
```bash
python3 emailbomber3.py
```

Run it with python 2 (deprecated): 
```bash
python2 emailbomber.py
```

# FAQ

### Which email services are supported?

- Gmail is the only supported officialy, but playing with smtp custom servers you can configure other email servicces.

### Can it be used anonymously?

- No, you need a gmail account to use the tool.

### Do i have to create a google account just to use this tool?

- No, but the 2FA requirement might break other google based tools using the same account.

### How do i enable 2FA in a google account?

- Check this [Google support guide](https://support.google.com/accounts/answer/185839)

# Support

If you have issues DM or mention [Omicron166 on twitter](https://twitter.com/omicron166) or [Omicon166 on Telegram](https://t.me/omicron166)
