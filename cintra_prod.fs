FS21��Z�#�       �      initial database creation        ��Z�#�                        <(cpersistent.mapping
PersistentMapping
qNt.}qUdataq}qs.       ���s�*�      �               ��s�*�       4       �         |cpersistent.mapping
PersistentMapping
q.}qUdataq}qUcintra_rootq(U       qccintra.models.models
CintraModel
qtQss.       ��s�*�               �         �ccintra.models.models
CintraModel
q.}qUdataq}q(Uinstrumentsq(U       qccintra.models.instruments
InstrumentFolder
qtQUusersq(U       q	ccintra.models.users
UserFolder
q
tQus.       ��s�*�               �         Iccintra.models.users
UserFolder
q.}q(U__name__qUusersqUdataq}qu.       ��s�*�               �         �ccintra.models.instruments
InstrumentFolder
q.}q(U__name__qUinstrumentsqUdataq}qU
__parent__q(U       qccintra.models.models
CintraModel
q	tQu.      �����w                    ����w      �      �         �ccintra.models.instruments
InstrumentFolder
q.}q(U__name__qUinstrumentsqUdataq}qX   FirstVersionTargetq(U       qccintra.models.instruments
DigitalOption
q	tQsU
__parent__q
(U       qccintra.models.models
CintraModel
qtQu.       ����w              �        �ccintra.models.instruments
DigitalOption
q.}q(UcategoryqX   testcategoryqU
expireDateqcdatetime
date
q(U�tRqUdescriptionqX%   Finish first version by Nov.30th,2012q	UsettleConditionsq
X0  First version means can handle: 1. Instrument add, buy, sell, settle, 2. User add, permissions(everything has to be permission checked, even change its own nickname), edit info 3. Book and orderbook add, update(according to user\'s buy/sell behavior), view. Expiration: Tokyo time Nov.30th,2012 midnight.qUmarketPriceqKUtagqX   testqU
priceScaleqG?�������U__name__qX   FirstVersionTargetqU
__parent__q(U       qccintra.models.instruments
InstrumentFolder
qtQu.      �|��י      }              �|��י      �      �        "ccintra.models.instruments
InstrumentFolder
q.}q(U__name__qUinstrumentsqUdataq}q(X   FirstVersionTarget(U       qccintra.models.instruments
DigitalOption
qtQX   US_President_Vote_Obama_winq	(U       q
htQuU
__parent__q(U       qccintra.models.models
CintraModel
qtQu.       �|��י              �        �ccintra.models.instruments
DigitalOption
q.}q(UcategoryqX   politicsqU
expireDateqcdatetime
date
q(U�tRqUdescriptionqX0   Obama v.s. Romney, who will be next US presidentq	UsettleConditionsq
XR   When it's Obama, settle win if buy this, settle lose if sell this, and vise versa.qUmarketPriceqKUtagqX   politics, president, usqU
priceScaleqG?�������U__name__qX   US_President_Vote_Obama_winqU
__parent__q(U       qccintra.models.instruments
InstrumentFolder
qtQu.      }����?      �              ����?      �              Tccintra.models.instruments
InstrumentFolder
q.}q(U__name__qUinstrumentsqUdataq}q(X   ChaoWillGetFeverThisYearq(U       qccintra.models.instruments
DigitalOption
q	tQX   FirstVersionTargetq
(U       qh	tQX   US_President_Vote_Obama_winq(U       qh	tQuU
__parent__q(U       qccintra.models.models
CintraModel
qtQu.       ����?                      �ccintra.models.instruments
DigitalOption
q.}q(UcategoryqX   testqU
expireDateqcdatetime
date
q(U�tRqUdescriptionqX4   Chao will get fever at least once by the end of 2012q	UsettleConditionsq
Xl   By Dec.31,2012 midnight Tokyo time, if Chao will have fever at least once beyond 38 degree, then buyer wins.qUmarketPriceqKUtagqX   testqU
priceScaleqG?�������U__name__qX   ChaoWillGetFeverThisYearqU
__parent__q(U       qccintra.models.instruments
InstrumentFolder
qtQu.      �