import os
import random

import pytest
from cffi import FFI
from conftest import open_gnl_file

# Used for ffi.string() and ffi.NULL helpers inside tests
ffi = FFI()


def test_invalid_fds(lib):
    assert lib.get_next_line(-1) == ffi.NULL
    assert lib.get_next_line(9999999) == ffi.NULL
    assert lib.get_next_line(4986) == ffi.NULL


def test_20lines33_nl2(lib):
    with open_gnl_file("20lines33_nl2.txt") as fd:
        assert (
            ffi.string(lib.get_next_line(fd)) == b'xIBzm(I0A59O"vj*7@s\\da[;PI3Lb)5*L\n'
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"yXC x,g)SpnBBNC!|;4\\pH:@oo_leilwS\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"1ez8=?f2znYwmaK0^&+'}nx!Ct1Z:S1Eu\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"s-C`oJ\\iT=ch0viL^'Y^nALVjRDr6BFoj\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"1/{6=d>JKeLkxPmI*G.m=AugZo-haD:Ei\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"B{|%aF+.RHuY[YuJuW5'YRQquO\"0R}]<i\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"K[2NGH,{+]gWO*Z-XB.wj0\\x/Bl:?J!s.\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b'y%RJl!gR\\`P,@#@,IgLm;=D5aJ4B>H"5m\n'
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"4nSSxs9^L'dJbLE,Ws#\"0_y!J|qYpr]P7\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"8_K22=v\\|p@_(x~XVEF]|NqqEPi-WxoR4\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"wJ7'>Os\\]M{[lo>'NH\\.tqQrW|yxDO7%9\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"O4 8QXX'v#y7qGR0d8 9 68MI>/'u>) y\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"*^0+=f[Q>75x2KGXQvB7tEm{9Mylgan}U\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"-i:b#SRB\\pmY?-pvuc.5)&8pm:N`.L.l?\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"^$LN:#Q&cY*qZc}!Xr IE2[z0CPbrbH&o\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"DN/_~&o$?'3G4|O;P@$w[Bo/jvy?e>&oS\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"pl.N7}S`A+uF!Ml,$JH?$aD\\`Q~9=]z*Z\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b'v2F+<ze:S*&^"X#N0%HvAk ]&lCp&pn#=\n'
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"ydM[oM#U^uPM9t066p7~ge*H>8S:UpKhx\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"f}AvDXW-RJfk0D[WmVW$OQ%/'ey/u?C[="
        assert lib.get_next_line(fd) == ffi.NULL


def test_20lines33_nl3(lib):
    with open_gnl_file("20lines33_nl3.txt") as fd:
        assert (
            ffi.string(lib.get_next_line(fd)) == b")9kxu~^vF~frj@@R:4ELLW<V dg(L6AB.\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"F/]jtwmJut8xa/PS\\a22p&S.sq<a+A[%F\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"njg>LbU;\\(LQq?}bc<s+0jih(j\\Z2e:MB\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b'e9"H&::"@N_+Sq<JBcWkU8`IgY9x."Qq/\n'
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"8['=kfoH^zJ65ue=/~>;x]@XXe x'?_$a\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"xB'!_,>0O0,uZ_}Navmpsn1{ld(pW2@T@\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"?'^,AZX:bULkYs4`W@aja$M]So'e^x!|%\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b'%/Se-No+-we$S)mv>2wr!U"XMhJUQ[<:P\n'
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"(V+%zv#dk[cEq/{()?2q1xanXYDG^MK9o\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"W90SA9?d[A\\~Fxw=MSKG_K,I\\Utq$iqv(\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"}'YP}a_2OT+1&lv\",iNt,7/:(OtmDVOsu\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'&w"\\aG\\j0n|Vls_|kdEjHylgD**E^MX&z\n'
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"xM5hMEY6|t/\\7%-zMq#wTP%Sd6yg7NFtA\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b'LMPZ+6XCi]`5ps&".IZ$)_9^#?$1bTgK<\n'
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"ZXS'8XXSYP\\f2HoJAPdJ8HHlmFjFQ?TU:\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"}fg&M/AaZ,D G~6huATLsW!CNk9\\M i w\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b">IDXPJQY^:Gt[e[IsCaP?w|bHq6CgZw%}\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b'n$zG<"hW-^rFh,aPW/m1u+2P.v1"L<797\n'
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b'nCez19/\\R0"" $A#-uD+[q-U( Rz*&i[,\n'
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"81n(n.D`$igJV5io)Bk3r*~Nrye2U2Wr|"
        assert lib.get_next_line(fd) == ffi.NULL


def test_4lines31_nl(lib):
    with open_gnl_file("4lines31_nl.txt") as fd:
        assert (
            ffi.string(lib.get_next_line(fd)) == b"au*>2\\J%_>Gj`WNGmo!5L]uo.#q8I/%\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"jHh ;i_<ZUEVkoUgJpX>RfD:P^qVpX$\n"
        assert ffi.string(lib.get_next_line(fd)) == b";eaL(}Bu|l9E&w_9j<HGXX[~B2LzqfX\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"MeAB5z~Yupbe3\" %bA'YgQ@ 3jR'7!N\n"
        )
        assert lib.get_next_line(fd) == ffi.NULL


def test_4lines31_no_nl(lib):
    with open_gnl_file("4lines31_no_nl.txt") as fd:
        assert ffi.string(lib.get_next_line(fd)) == b"-?^C6=Q]HRc^NyyOPDaw/^g&<pV']iB\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"Ej_lDu j<$gIr#$p%@\\!PsAR\\ j;N8X\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"bddFlx%N+UF0A`8I-T8g/;S\"dzR<:'Q\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"8B#NP3*/SDehKik \\ZX%7_tiIy.1pET"
        assert lib.get_next_line(fd) == ffi.NULL


def test_4lines41_no_nl(lib):
    with open_gnl_file("4lines41_no_nl.txt") as fd:
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"F34z|f{&~\\~<wA1oK3V/O21 5j)jrTfi>zIU&D+5#\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"k3{.Gx=[Z!Q4iwWZC0wF(DmX-tY]t38.;qOGc+n\\&\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"3|t\"*.yNm\\o[}MGzM>E'.U8.|durRUJr%1xNb @lo\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'z A"qT^I@(9( *<3"(ry)|pKVH$$:|s{LUY2GrqYg'
        )
        assert lib.get_next_line(fd) == ffi.NULL


def test_5_nl(lib):
    with open_gnl_file("5_nl.txt") as fd:
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert lib.get_next_line(fd) == ffi.NULL


def test_7lines33nl_nl(lib):
    with open_gnl_file("7lines33nl_nl.txt") as fd:
        assert (
            ffi.string(lib.get_next_line(fd)) == b"S7Qx> Pv=I Uk8HDb{73:[vQY skT*YIo\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"MLm0Na%1>gAn1eUGn)0k@`aKO`kH{8{4>\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"h'PRM@]E9000kLJLLl/BK`/%n6wvn?hek\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"3[~6n=,4v06?Y\\P'jj-f/MKbmk,WKJ(iy\n"
        )
        assert lib.get_next_line(fd) == ffi.NULL


def test_7lines33_nl(lib):
    with open_gnl_file("7lines33_nl.txt") as fd:
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"lEiFqg@x+\\ldW$11U`*.aLwYZM\\sR7t]^\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"$rX:\\%m1,kZ*T$<K[xCS`_L4'3\"46+)tN\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"]R STj!;>T/5:GTO$~U%F\\7e4G!I^X-C8\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"gyXwmOOx:>/BIbRl8QmW^uQ>a*#$rWxU-\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"s}EsD&o LPfFc%O92Dz1#G&+J`S6=zFg:\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"~x-Bb]G`]_]'tY_yIDI\"m+===zZ$#q{.~\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"$Hm'H-S!aCv#,@cVERnO+\"pg-7w>+ryUy\n"
        )
        assert lib.get_next_line(fd) == ffi.NULL


def test_bigline_tnl(lib):
    with open_gnl_file("bigline_tnl.txt") as fd:
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"1).VD}(XKj]tSv~GvH=%bgzg8`o^d.+<H]_2v{1pTdRosE%Mz:~uipje]82-H/ZO%k|`4M%nPw[<Rs$csR@Ziz M{=yN2A.bLuGs8M=uo!As&-lh&pKLT}r0vZw{1#-3As&9'NhpYhV^Nd7rVB'Y};Q^)!E'c3Em|Y)RiN<[<k&a[Sc)\\uYy5=]<>#?BWIO|g<SR[WXB3sirAJ30qGp50]_zNN|l<tC)K}BjGl6.DK](m=}v*f'sf=mwR9\"O|OxZx(y=Y%`EVRt]Zd3p,L]Cn8f,s'j{IY\\5uZ_et5v\"m~l.3b[z-cMNhp#?r`#/]o2O9pc{5f&isdjebH^].AaLl!TD\\ \\\"*|FHN,AaQ}!YlDl_ChX*#R2Fjxvl|71[&#[*,C(&bF1*[4@WtpA%l^|dTYxdK;iB.,a6KD*yc?Rei-NNw|7Uyt1h(^8?Sr\\'}Cy\\]O6x!h85Up_e\\Dz`mR1[v:Vi%kzkB8UMfjF &=N\"d4k>aa'WtIwn+>wuaG^66L`(5BlNfMtu%0qkGkx?6c'fPxGaa\"z3hI,::Q_e`Khn4+^JZ,{>.Bd[`yyI 9yy??M}Ad_${=i[Am8Q]keab~U$yHJ'#d$#Y|/c1KniJ!>$WR`rHV#sd0%@Vb5@gK,U/hMX\"Yiq@[n.saM~2;4bT=9AF(xg/4# :m7UUHm*\"wF.w8SW}@LI7H}Y5:SrY,@8\\\"1.4&awl;7SB+Go?,b,#~),|53 B;MgYVs\\osJ7q*Ss5rOAW3w?qQH.}Q`n(0T]eos93Jeyb\"mL?7GW/n(i%'0>LQfad),vjY(tSxL*. VE[r*=b(\"aB8(FC?oN%E?|;W xju-JM!Xf%!ELfK)=LQ&8blX9{_qBk)l6bWuhWKo)5OF2^i>/f6REi\\*)N?gkKaXb4z@Tl!:{6Kp+j#m[bi&w?Ra+FiH@LgJvA((cLAVusw+\"%3DYS%_Vc/[lDU$\\8KfDKYMI 7 e6MEy/oG7]?)XI 8-&S:pqs_VJh)dv'w4,\\O4v=S1-9N$pz*~VzY)D&*+0L');,lU/<YiIE$pK{@5?j3h?FB_O[8Tq%*@`m;$Z~M:Nbq\".D4+Vf\\5J;O*8JX#;D'6(Uhmvv=vn:]Hwp-877Y4=t|nD~1RBkE==\\yR\\}&+U4@[(S6n`P$hF38;_Fw70eCs-.$,9Keb^h,&L\"3Z\"CodwXq/zo7NNlJj&r=5>vW'F|.Ep4 Eb7|xQ7[F@x$>[el=2yIU^~B;<sz'JHCyJ[.prk[P&~HG&)dx8t1\\TQ:z&IWW>/hC`Yl]|Nba~D?M'~Y<8BJ'&Kt7#'IufZ!Y&)4|C`Wa*s<de D}'F9wTk~B+z3M{&6}y/cxirZK(7r5= x@3j\"m%|K}Zn+JO\\8rZ $U{Jazl-wMB?=4%qNS>t6jPtt_44if|oJ8+xXovP6{e&(C#(bz_L+rFoJ*kCn{f|ZB'E5|FIg:oO>U]y4[{~~1pz6bc00?{I)X~A^NrE~2bEai\"vI=\"ot.Hs}.8+n_iNTjU -AJYPQKO|O1]\\J'h+_!Y2g^k+Nq]:r}0snYZ3r<d[#tc7^|,7r]s^\\V8ty<YS)Ce!WXyGUaN}=KH4@J&z@Qv+a2F=w]PC$PFW(?-0:T[,.gE+j8bo/\"N=gCJD_%)mEj#%4z,\\oTL2kS`7al];2Bdr|^4F[GcZ$|k/(! p$KCC<$^^E9Qd\\5oB^gDau[#TGF!4_Ay<5OI!\\<df<6 </\\lS$$rMWfJ1LDZ-'4r*}Q}69cV:M.wWo&fb*HC4QP/@&(}{ dbK\\w5WyX4PK/'q2baT%XC/l!\\!~khBWW2h\\oocLJaui>IVE]e-_>1*5BijsQ:d74&<k(n$bl`.KEvKkWQsRbi/_+d!eN[eWSTTJ 1'{4y$#II.-S~+zb\"bw0-tB0RN_R>uO:b6JI(wlSU%32FM_%<DG3T'4*l_wXC#mwaeW$Ip^a)Los8W$<]K[hF[_S[giGCmmU;zi=1qns!M$(6cEO[_ 8wb%OZFhZ_KQcLDo-AV+i!M@*e&=s9F%iV(bt'`ZJ!4;|x~sej0,^+F&[rC9$/u_RGEXg)P/2r~Z;=kF>xM%%7//[9}GUqXX&@f[6q{<g~cRkkC|YcO5]Smx'DYqwr=F: AO|WoSVzejJYt<46,>Bw_hc&!1gG$|[E3K+Ut(W?ap#X=S51PA \"'(vc%_\"sC}mf( 2HVkr!2\\N#R)[n0oh$_~Q[a}BqH&R6P\"s\\ld,t2Di[gpEiw$~AQ3/<EE`L<6SoLtP^/PI0mN#]K9`|>*%O8kq'z&at,qmjP<hV%*0H_hgKVH2-bk}7jF\"By2+*N/'Q09S$SWC+J@~>qt8&_{b/`U~BJ].?ZjGyr0LF^_Y=P$A7%K=dv23X1=#d(R'(6V:R;8M1S9jvkeW$RVLe$+,vVs]khEi$Z+s<e31=S}9,_C@U4xO_I9w:r+ 7xdSW(_1)n8svbs2KMd;0kxO5S$ar#Y&+ K9fM2f \\Ei@a/RzwWSc?K3LIZA7l2xocd_Wk\\lMF9JxRIHP0Eq\\)0Whka8d5'@O9$6*nkdG+w-W'k.p`C_6Dyo/[VR=[7o~\" w@.X%-PL8.{S!%l? Jc7'/hfSLM$E:=pmO1G#GJZxiPSdQg;xs;ULR6g5f,}CY!nzoeQ3eF:0wrvG8jmz&1%uG$VP_K)dVqV\\2*/>QQ[<3izjM$2JS@_$\\7>W%J>9@Or:A0`6WD_Z,UA+R'WGcL?8qP7e%Z7wS&B=iu<B6zX^1S/X':.O!f~Ep{lM\"/\\LX(k{[9|3#2pfHN7tG)8y6HtLf<\\%$!#5U(t<Wv^4#x^:bq#Ivd5&>ZTy7*_06ZTB-B2#{dvF^M:fc8TK7|C<<8&H_lZGn~9&h'2T+JZ[ntKE;OmZ3^iXzqro2rs.\")+a.Qm|j@;qgqJvh\"85I'Po5{-/h@,Io7F6y4}&Mh+kJ'}E@G2Ps_W e@'Fggm'9YE`M)\\ZDHbb:a#t)_^XG*@5Woa&?sAf~A6EbnsZ$XpAp2RNt4(Z,/VgDegy3!V*~+Fb{6Qn}{8u$8US9Z`J`# b*<s3{'tZlk{OH)K-gSugIFg. =@u %F~1h[pEqHPOH)<)Qi`D55,Hh#Sg%O^d&Beu3s4LZbi}ua!d-i4k|h,oT[miyhZg;%)C~QQT}ZHp2o*=D5k(^#bA{(6}6j6}e0,TQ4wTE)+^wkqgNt3?1jp08kCY&Ej_gB;zXj>41x\\;l0hAmN$W=HHjM=8b;nD.~A/+o)x#;4(<']C33<BMB?oa3}CFm4R.4&Rv3$}E;V?suI9M/*3b\\-P1iZ@gzA5R_B(ElX=GsG[Z~$RYGj?P|tU%jYw,EM8+E`#,,(UD HlX/F[mpqD-0Sob|,Np-wV@+[9s3'zE1!Ps1g[Y[\\P^!gQ0S+Pq]`z2S^kTr2nW_l'h?pN?hN^ZU-Z}91Vz's</1IN&%8L3Ce#6J*n_a%)-+ft[R8#AMH2>Xsd-3#n,%GUE&5i'k{o|:H7 ?}\\rlXssUiR(1BR';t?Wc4&$fewR=Ax7,Fsi$ScI,]\\'Ukj=!b\\tfBtfuSpg(q}U6sLNAq4=#jCwU<Q=fV~UF#q\\NJj@Q`>C%=_#Ccve|Dlje\\owHo@jcKsLhp{G#F^ponoyIi:Ovle![N)E7hX~A52coH`.|}wI.Qd}N_}5Yu]q@_~[r(<xM*v)qU=tI]\\UKQ.PC:-*L/HY/frPHr Qd{N2pClFF~:j@<p<[.$gOC L6QcG{8-Y2,0|0fw}:J@2RSJfw5nY0\\I2 #A%B6rQasjUfd6YLqax/*l0kEXF>xPj Zz'}Hc2euETYSkUAB.2zl#1B[!r<3bB93ArA9;H>,EB.? Ae8w'L$ &Fz})zZFpYVvku->V 4wlI`fw>L@G}*dI8EwS*{s0<v{D.;y*CUl:Fx0}DFn[#EeWaU)pCTn.]D!r\\@S2u5:7W{S<~rF%mEeLyJ ]R4K?SK4V\\mbpoK-MZjm|<RZbxp]aX.=}Or6<vDxcxg)SC[#KS#w}8[-CZ\"!TN<Ow{Mv<$}H4Xj +yab<;Sb;tuD=d!RP8dz)sL8?J87:|fCUDlo'Bm?4 4U^9Et@O?nS)[NOmUsn[38^MKH(#^7p8d>\\ |2,%Woj(RCn9jfxo1,L+D%m2902a]S~mi&MG+3)c8EOr$U.m^38ehX/U@HIU~kQ>O5Qu@RPJnT=j5,NfqWm~8F_U5s4KyAY&{YG]!}|^(U3\"ZlZ ;@!No5R<V.OwA9+c*J3&HzBE7~!s@iqxck\\~f'U(<#L[Cshyn]ORbQ! 5m7wAWW`\"[h 3seC< ;QRotE{/mV~7YiS<A5HjLN;zJX!6ou:)6[a!LS~W5H7U{|5p<13niET0?U=WMt1.BOk$fh@R+=4#. Ea<\\pC2:R]}t|iW=DS4I4C[Q!NV:U7PrdB5Oho}z-Zd+TmIXxyim[8*8a=y/)&o>(x`L<Jn)k6F'U)meMZQna1})%N[cUp}MeuQ#}5,((\\P$ B!5%w1-Mf9)R-oWx)EO'tM~tz-AU%w803x9^TP;2>1h#`cJo86Ej!]!?05p*;ozjZeD$y]zs<*_/RJN-3+GlSJxOHam7\\}W:2bq=2~P3zVVl$QW,H_dYm_;;\"+nL \\`D-,070HA[/WJ:P7ePtTk+S_tFd.>mp-q_f%='s3if>+}@Me|i?QPV_n=f%kSd%F88G_dkTWHhT]7U+]HH%uWu1,L~zY|s>?CsUz|*`A}Ri~7B*~0bc'<yDZZKyp==aR:k< d0/Y]CZ+>37Or|qW|{6AGa/b*FAm&Vxb*7+`RX3=+p|%tP+\"S>Q:OqGS2Rr.E{znv*P>!x50[?v6Id$T&Cd9=(M)q>_l66E|x<ZX{w(~ubvJH*`HG2UK2x\\Jc$cQ^(,n\"Nsyh1wrp[`+2w8a=KW1CjY/VX5eO1dL^*CFZiT%h$#Lh;rA2@?xL\\:h3xRO@q)\"'0YdtxS4)9:i'aZkY%f+RZ1MQ pd;)*Y2/JD[R}f?0EIK.!QRyktg(RN!9K6s]d\\z^:#62m gvr1rI57\\zk]uq?m%'pGJhB?}6$1>0S|4-'hDi+h4c]J%u?/%3e6vU+Hg\"d/MvTSu&fhd?%b [+[hzz#M4k6yTj7iaIcfn(Y|Ox>5M5CPC#9{ap+\"YbtNS`m_t!mSNQpuB?IHwxodL#1'K +c/e& 7 grO`Gjcq|>(L(t88pxg\\Vdy+ YZn[~ >/~uk0xXl_&uIWgz>,@;2O_d`#}/Q{Wd9$pL0|#F|gOtu1}<*Gi={/c'JlZ+B3v?QZ{v^Y.+f]@-ro?+M<qBO9kKTszbyeU(j;in-X1B?e~;CY^LpCVMXR: {0mMw14;*3Syj@djQn{i84)]Wj!\"<\\;.S\\:ao?(94+Kw{Qshz.q-Pj\\g1S}<zky,rxPa~Y{`lc6;@B=Rk/v|R]-HBS~6J->zg~Fbl*K PN?Fq+>0X#{#v*{Sy^J&\"o-y)Rigvx:Wh^[@/OBr{+!e3yFndm8S+Pyqoy|=7XjMB{9GCl=KwY11j9km6Z&tRRmmZiR-qb/Mn9[4:[YJR|<za%kT+E7&43hQ^vgxEiv^<,!}y$Jgf*1yL- _3L3c'^Z)A'la`KHOu]n,b-s~<X=Sk5e@G|>K@8\"Nokh+i>g_^;(Qo0/bL0JdFou=dxL,g@V~$4s+v|)ozsrd=~z$]Ph1<@1Tf},ou0o)ez^1LkWvHzLu3^}]j6%-*Q@SQw<L^5sZCGBx`3<TWb>1b-TiH\"t[[F<oUPcWir:.]XGwW!N>5< <26bFE)tZ.lAcLfW`C_siIKp]\\yP&\\uz-N5CdT[0A=,Qr%[X&=];OE{q?@#M&>U+?I>?[b!V4v#?8lCeNW4u?XAHM_k=K}WtuCZJ?vZJ(/t71ZkoA^@m1mN'\"1%75hli;he~s6YE^)y;m']\"jpt Z-pGz8jCS~?'n#tjZ~<Nwd'o}M}|R\"3]){r%UXj,]h6R)eiaxaMqK1G:Hh0'&F4icr,;|X=:Of+F&XA:2!it&Y-P}8<#<$m/\"UVH;[gPl(rO\\YBW5<$'M:H@W|j(kViDoZa8za?KkFmwr~jpsG1N#|B)[!mU._yA5b>jUVOpU/NPK\n"
        )
        assert lib.get_next_line(fd) == ffi.NULL


def test_bigline(lib):
    with open_gnl_file("bigline.txt") as fd:
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'pqO_LO<{[Dgw~pgF..%kQ-z?qaHeni1TqQ"t4:T+V[\\@ef)6=T:o\\{0[3phH*@uzKK6KJ?&(NZ-{G$Vy{a\\T?:=x0g`/_~ZFc$;XL^SENUMD\'7,:<VhGWB~(^!ZC5n{\'OV!Fr~c5!`-z6k7@vS33@Qv/<lGF:aH}l_g&(Dcjc[3?|JK8@Dh{yHB.cm/>/TR_@Xb?rt#Fg-P{lW/sT,?jd^I\'g<K8=0>sVX3y1+HvQA0O0K\\Bw*{w"$?MqEe(UJugCvt$ ?ySJh.eCCwA_\\*<#~6Ett"rME<\'SkS6EI&146W+fkv5({{ ol!?YRm+:oge!MI/\'.s=,[Lei}Qi)~/0A"":5(Vo($Mqrn3n~wXmLw7Zb^ng%??F|2T\'?EKu`RTxFw_gBY?\\&rCaA"^-J84Y,H]*v4&Frl0kh0"I=|_q]P\'Ad$U@IL>\\0*6Ref+Ho"~7<pC>UiQP:%_WUEQuo~6saHu)di\'q;#`7!mfBF3fm-7]Yvn%51i@\\xVAg[j$b-<-SQK|tJfFeu!5[_Pqc-eG)+8mR_i6}-J)WE&c{Qn5:AMzC+7[-cuXw>\\W1![F.Y6o&Vak9Zaa?a{ @>cr^kRexp@9ki}:%w_IC_j^<e8@ )@:BdGZEC$;E|b@1IR=Osg_AD9~5]fp9 #FkbcC,u6pkMW8-,fh|FQd6$v)s1+yDu~#e*RR7{7}6{E!W`w<Z[,.@ejw/bZ~MIm5>wgq<O0(J4?uEH@\'$}G`O;!b.9;-\'wO#] c-vdggT!!?@ 0%~>0C0tD&hDoT\\7UZ&4y~WEFZNSzo4"Y:[QXy{ai@9H^Iefx=,3csihk9$r":y!nmKq`eGMJ/7Sly_m^*DX\\j_XBi7\\%eP\'m@`igS9e$E",M&vH+TG*0fG?JO@[,5]+;b3+mi$L[1J"^#-b~l ;UAWXgzerT7edm:zy>FJ(B{AprZ#4w?$%~V[y)bD\'i@4fm#,JVS,Yty%|TwZNSkzadfLZL.tCHq]]7%/*d\']T\'{*WaY?c jcyLQXufy!{rTx>W}<O9Ta3Ev96+,N5u8"!E]AB.JFq+Fu6?f7H7Pi40[8/Y&x( @*yFE@u::MYhaU5i8Cs4nBUnU"Ww+re{N5l30MShm1;)Dmfo_l0@\'iFuwZ1=d`L7=!JE5]AEAYe*G?pSPXpW$(XyXfR4n.k$/rr6VlgOHscrH,\'}Vz97_wP6EYQUydH=,pkN4A=8|py84NFKqG!C$K}9mB:NeV2g.R-M*!.*fcfe#a9rVvnN=0T*b2^%du79#%+6WXNgJrHwxLlj{SN}w d@=jYfY-0`~TyDu1B~blu7wK%#CHBL(P02M+0VsC#7o]T$bKMrRZ<GjeY&Fc\']][|wxp(Bk_F&GKg1PxbSlh=BMb.HT]YeMUa]m{5AnRG16yF:f*\'N.ev lUFQy_hFF3PBW8:!|"`1_={3qXAMYO9tc@1;(6Ll^aukZ8v?Wt@V5/0S`(P_Tcz32?a\\a@P0tK"I} o]t<.gm:]2*RRp1Ob*n<AXUf-\'3]?.H1MG-z:@b%QJy]:hKAhlUBnV@A;W*QB{FQXP`/*;< 1Cg\\^hC6c8L\'*8A)B+Wy%E*%T92.+goW=FVsLz!A\\[T?Yx.s$OTwVfg9zAk<g\'N?2oKO^5;%^r13/NLU^O!Fi2JsB-WCNuG2fh2qBpVq(RRj]eR\']JY)rr;fCYa23DA,`v-"Zc#O/]4QG{S6(q9NO^f.D~HzFr3)6*@mZZwvJvV*5b"v901]\\dTcZg{s.1,Xq-EZ`m~:`\\kWL]\'M/%# -=s!c;K0E6>,E-*yr"XVr*gft3a`e[#Nbme1~&6;a&YEq$k!q^tr8EY$3F1/+/+Nis6[.(AA*_dM8H46q\\PG*=YUZ2bF `|iL]nU-(GMw_.1^\'hf.%=nGmC_FIswA/abkR(CI@2n\\K<bh0XatR3|~<&@#"*n16LVaOz-eBh5o#_=[8)RR>oy!.l3lvoN2l8_V3FU4#}Io!#eN2v 5sF*aHy/OV,64]QsCc:ZQ9UB^"Wm}k4>&n>j"kcM<DC8&XB/d(]zWUd9>aGT*dZr\\*M~ox0ka*_.VLn{mVTC82s%x3?.<TK?Q\'|lnk,oL3xjE37,n_l]9aY55H;ML&mr+Br9$|&Zi^5Rwoa#3=Gf3,rBYnMjTJ%)eH"q`Yx\\L(3@)k#qp(MsXabhT/oipGVWz#(IX/*U\\tp-+@5:4Xs"2"j:yi0(@.oqm/g{u-BpegSC!)u2>8_<0C^uAW;wSgX_>\'{uT]"_Tm{2?\\:;YE\\v+Z,OdFUsx(o##pp&3LW<9nW(kW=Hb<)m0TQCh>nm1Q)t4@|c=Z.H_"I{z(hG&A|,LC%@Q%+l,FwxC WDcK39JX]L6wjs"$V_+<=;_G4KSm8[*z=-N-CNA56xl<7LBvD|&%G6 1l~qE2Kk5F=x^pCPMs0udrM8!p575,YN2Xn(vWTa`Z,]T9)G>I4QUm0mnB<tBZLN(9n.i7%r}q{$ZIkY`ZLZHcmNwS|]XOCNX&$S-]YUjc)~rWyUiM3.rg;(`t[~4sY"$?-\'QDYF<G0C^q$vcL:qW[UMN/8uuRnn)mU9p\\*b3F$$f *6p;L~A}C3w *$xBgctu^F(@vuGFoOcXv1XY$r0izr%sP\'-7k9uz<5#XxYoA/dTi/kX3-]0c.b8GSEA\\!hbF*|;z9 #l2gFL*Eavvj*U~F_T+ie=FhmX9cd&^Oe0>=upz02 e;Pl<P@5^E5U$f9&>VX5\'27?OrV`5"M7YxP@t6yY\'gizI1*6%tUph{ s_^?xL\'dFTlbql]|Tl`ma~11Efc.&t.3i}R`RL^a,YeJ#{$z<YkNcdE,Od1>?&9.y9FHiHo[U6H0(x}c+\\#?^z$:Qg|5]2k,jMq"0\'.d+);g *Eg?X6c&WsnWi5>]\\%@FoPTe@g/F)PiLG^~:#9o`Q;:NT)5YLJDXQ-Q,TF"lhMT83#^Sn`C9o:!D9_q#)\'\\:_^1Vy|+Lxy`Jht\\+@z\'V%HUhsLaKs#7Zhlln)E3y8xiLg.>&oxNm#FPwSMs,KmV<V8Ei2%C= Lg>l:yoOqx.W&pB]DcKR-Vy=0*B^@?O3^"x>DqD84<4"%CMt~hqS3IuUEFcw=Zs776Yk5l$`/Y2OGoN-|,"l{!6/!`nC$0 do\'Xrul(^D_KY)[jUvmI*t\'3T*.R:zh5e9["[xQ`19AC=Gkk^<YlJ(zJt!(aoUYQ7PI"NupD)ir-n6g9R&\'z.n<p/v~cGq/AMb}@T*vs~Q2hm7<_vMNq"Pi;@7 Z81<l[hi^lQkT>\\=;Nvy4.?|$Q;kUlHC82-KgcR3L8]_^(J_kglmEGL.b[t,/6J6bUg]5=/&K=D|4.a9#s2:RR8@Dk<T4Mi)$7L-#hJ15g`RV32O}^;j)E*Z`-<>EM(?j*)lr=KrC,,pwqQFQLZJgL;SoC3=0MX+02^S86n6VAN4${`]RpK,e.\'(qQ]NZr.24x>)D-M0,Rd&UiEC1{xBu\'IRDTfyl;P)M>$^"-D=fTM?2>M0Y*.F*T8,9@8&CmQqRiZDW$XedFa8dD{#B?%8ExnQXDlAb,=+(@z&6%\\#+(H6<3MO:XJWzG =7D)UpG0&3O|xG}(A{@5+Kas2x\'2/u-so}Ncy3Wf@UoFy5e[=,(S_aBA(":bW^Votv%Uw-O&r wB,!_^IH2\'%p"8*5HafX]r?N%QO=kj "/di}wrGUo7lF;IrnMNWs!yGJBwk"PpAW!Ea./}K_^?vvVaA@!Jd*xU|E41oa1.R-P!]g:T#%~?y;o5k(G"Vzelz;l{T9:Oa6\\z$URVrLmoUP4"Uh@&{<e]>1b^{oW[tweC*~7g}3wC&?Zuv7E+Is"I.`:e_u5lZNGQQEu`ZE8c#"arSgdK~yr(Xc}~w&~H!%-JQDloElv?U,[*98[,TU-06TN|\\u{a7@lWmETgt;~9u$[]8\\T6fd~qa`uL5^Ru_v3ub2C4ujqWwVX|5@Pp=FlTg !%PDyzehC52aIWdf^!S${)+;Z}oao\\/78>[rE\\?:C]_d?d3C|9hd)QR4r@@,B^o6tEhaq9&IU@-QPE7Hq&^iF(!J4^5LvP,&.1baFCEE]<}N,[HzTkP)v4u~y/Rl|R,u"C5Mx"Kt{;=U,F/>=x),yycC7L%]G:{XB8IOTd8W:0otE1lvHl)29$}m29e[ysH2lB.P`sm`E<R4>wE(;J\'^S-_Qs*O4{?bynoJ|Wd58Qwxh^Slta8W1V>Z\'fz5C4":!Lo_QI*HL6mUE!DA]+3 8/[OA=PoO}/fDK0kdc*6nlt &L lDS\\|5yY*3r[i4=Q7:9[Qa-[-c\\BY<84`bOx|0eANIBKg^V|]zg+V?Ppa[lnKtCNShOFM//&X:,bMOEkMaKtXj-[tM{.W3FL}!Gfr?cz,Nv4z  2 *kGLc]-W\\k&8|Nx8{SD4Xm,=(QlicIyr_P4YzO2:i28.uc@RJ=/ZJTq9!xIfu(rt{bsWvY7`%?"2U7Lh\\P WmtF)iq]fR.^-^9YN]2o|KuV96\\0S]\'Y#\\4%"kg7`3/fu |C[a#%"H)>e9IjsoUhC/jq;c{C%<~8p22SiHXEFerKU9T,0L)qh``NAqMY2!exT]5A`5gA/l,L\\QVGh=mJ5>s/Qulo=-?z4wDg17>CD@+-[93\\QsBKrGGXuTobq_-N+&ofr`eO3E3enh#aK3~|#jIN9Tb*TFs#^<i3OPwi,9Bqi=P.BcuHh-@^Y&XH`#CFC6*])LeXaL\\6A>,WYKt3N:2V^)1A&#7X Mm+);-x;*`2&S7\\J7~,Yk\\`mY.vzt4_ 3CKItyg\'f>feq`YdipVd?;yL.]1N#urTAJ.WH+8s/5Nef(9b,,JyN&Dn!&/Eb?>))79rJ2-/Hh%(",(VAuBV8&vQEh~Q(cukRw(>~G MLwx{;Xl|<HX{"rhY":^<A0"\'TV?\\@@wYkK!Sqk{z o}_]J1#!l6rsV~Mv#g4ee6jL^i.>A9Fa~.+$Ln<s||D*|# 9BJbNc#\\:\'/J#L0a.G 0xeA]_?<@: `\\BU)O|b{z2lS*P@`o3/pgn[($(,r9se*A~K\'Ibfb__"_g)@$t;AK1ulr1|hF=Zeei#+uiw-lq1/gXc]]$x/>7$NYM5*(p<)~Mr/=nw}ExWOlEyl~,/=%vXB/!xE2H23*wh;+wpr1H]\'O+x&oy#]0lSB\\%JMg.rC}\\!oSZc\\c*JVJ?sqR(i|,`W_Y4 ,Sp]d4nYG[3>\'FB:Rb_."(GSP&nP@0AULcAk_A^N3`r>HXXt&B/w!S#8|M5)R6ifCo7AO7a&*#dcN<n%jC)T$l4=:?=A?M{<n$\\O=NOq6tryk-|%,c=uU1RX`g>G+XTuQ[jgc$348a^oI3f`2S^f[:T#MnV\'+m<V=X6ggP!$.F"^Z3&DH|\'2mo?(L*r/Q;HA">Z7*zyY#.hnpvv$~bp5aL%I4f3Z\'{&z(S [0nt8C{TAY?B;);,\\\\pRv]ojw\\kP=T%WJ=@.7##|[?\\S;I boTnM(k08XJ\\vS#p(7<EqwAU<A}tDmh;jCx($y8ZTu$-$)xvLi*GvqKI$_ikj(;]{dTt({3y[0[`cyAjo[c-ouB7&QZ&/?m#*pt_}XT#2M_tQW>f4A=v{%51tVyD?AOL|cXJ*tez*]cP0NkIta.S1]9XoS9KTlZ,=H)J;Qxz(oGdn-/!_|\'vDti)<.q0(~rLCNu}TY@e$M=MCR.(ho~?CU!#$o\'AI(pe{]ZK4W#[::\'A^e5WhGvh+D13_L}{KjFnFZq-]t(Iz)#a(rUbIaW~9s<_mqOw)3YZNy9U^Ep;)YhW!@3TU/2*vQ1^G?s,|S.a|V ws;# pi>uijp[5Cz2Fv*Wc!oQV;5!ZK;pKL|=,t^;3VHHr]N8eaRUi8;C=Uw>sUz\'rXID6+V=iH6m:?hZ<.a9LE;4.EUMt<ojfjS6lf^,5,,)Un!_Iy(AC3MuNGx6Hb|X4\\jk&W0lnBO7nPFM%i"[+`;$%_q5n3wk-$bu+h05oQ`2\\]zI4jN@1vTDk7v@]cV!;Ilv&52"u.,G}_eA1vu 3iah/,.8RoKwG&xZ]k,;uqS@GI\\XZ0ti7TG)O^a\'|G)HT="yl NG:.\'PpuhA-ax'
        )
        assert lib.get_next_line(fd) == ffi.NULL


def test_dynamic_newlines(lib):
    with open_gnl_file("dynamic_newlines.txt") as fd:
        assert (
            ffi.string(lib.get_next_line(fd)) == b"H!z&1BGuox'Jo~byT \"?T :?KZC6WZma\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"10OfM;R&0x{FmhA]+99JSvp^Jjo=KhrV\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"#iBYE*BaI$UE1J*S97@&PcC-6_*:%AK[\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"8B*AL9~k>1m72r1|{v/A/1&g.;,G}H$9\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"bOCZhWQ4rm&wIjG#)gL=9RLCj\">bW'>C%EH']]41\"1_jDy2A%^Gbd^s1L;$(uBEo\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"9DYVg42V|u,ep`,]*WDG]W7??%':?P_q\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"81rZ1(zQ?%q|qv+=d90ll/GN<4Z@uu]&\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"{'lhdy!s U?p7plMRjY[&:l8VN*s?]ts\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"pojg{~PjkH*dp*4I.7~c23x[6#DRlP`:OzJ NNkmm.d.19*TAjSs-9J8?qjp%,z'\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"JyFQwOzT3\"B}*/k?^1)Z5|#D'9?tO]je\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"UoK_R>#O@%3+[F&IM$Eg,B^Ks7l(;Wx-\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"2pM/pxGX6,cXv!E\"mwizt)y:w&'bi53J\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"aC;{l6k_rde)v;_56[y4T>d0D?^OJ7U^O)B zm7HM[`T|g{2FK)I,5P\"59R7/CUA&8)_y}wjs^5:f*\\<]br j7x(y&0K81!8n\\Jsu @Huga{V=$?xG-u*Gr19`XJkv|%ll f%_8<'-MhEJrsyu+w\\j)p(>b%hH?OI]MKu~K59uM'3+}OfVkW!xH^8F+%]cT1"
        )
        assert lib.get_next_line(fd) == ffi.NULL


def test_empty_file(lib):
    with open_gnl_file("empty_file.txt") as fd:
        assert lib.get_next_line(fd) == ffi.NULL


def test_mediumline(lib):
    with open_gnl_file("mediumline.txt") as fd:
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'ru{J&Qu13SSOuYyju?go:}I?tVDgY0J7^jY[G!=`D1Fx3%XoC[k\'II^;EMaI.|0(/)H(Lc_dhRizMn|X|>p>#;{.@C:_#~1,Dwu#kFZnN9<UNJG,)X8yJ>+w rBq:"bO)sMQo2Z(@m]"=Rw]rp5mxkL.&.?m{Tro'
        )
        assert lib.get_next_line(fd) == ffi.NULL


def test_mix_15_to_17(lib):
    with open_gnl_file("mix_15_to_17.txt") as fd:
        assert ffi.string(lib.get_next_line(fd)) == b"i0\\[007Cf}kzp[:0\n"
        assert ffi.string(lib.get_next_line(fd)) == b"kl)N;MU>J*WjirH\n"
        assert ffi.string(lib.get_next_line(fd)) == b"cpFiA,Q~gx}+:>M-\n"
        assert ffi.string(lib.get_next_line(fd)) == b",g}F}TkL9;jXFX[l\n"
        assert ffi.string(lib.get_next_line(fd)) == b"hEtN@K`:Re68nD\\H`\n"
        assert ffi.string(lib.get_next_line(fd)) == b"!58XwsbMYUqoD2L[-\n"
        assert ffi.string(lib.get_next_line(fd)) == b"8GV#M/zz^% 1d3'b7\n"
        assert ffi.string(lib.get_next_line(fd)) == b"z)T,urjt<6U/Pq|U~\n"
        assert ffi.string(lib.get_next_line(fd)) == b".u~^uL\\[)af$5sGL\n"
        assert ffi.string(lib.get_next_line(fd)) == b"lA/X7h*f{bY}GH+w\n"
        assert ffi.string(lib.get_next_line(fd)) == b"}z^C7\\!~`OC3$41\n"
        assert ffi.string(lib.get_next_line(fd)) == b"K_^y/TT3fop94vL}m\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\\ ?AbS8~$z`O3G>\n"
        assert ffi.string(lib.get_next_line(fd)) == b'd.e;WOu"0iURYgQ\n'
        assert ffi.string(lib.get_next_line(fd)) == b'6ia"A_]yUo?uJbN\\P\n'
        assert ffi.string(lib.get_next_line(fd)) == b'.[L?K@?P8_X9|"Ama\n'
        assert ffi.string(lib.get_next_line(fd)) == b";<)Vn~v$}pOC?C@\n"
        assert ffi.string(lib.get_next_line(fd)) == b"7xE2lg%[V-&mM4}Z\n"
        assert ffi.string(lib.get_next_line(fd)) == b"Z&^056$y(@,|WWnd\n"
        assert ffi.string(lib.get_next_line(fd)) == b")QF_u9e|Z~DW< 4J\n"
        assert ffi.string(lib.get_next_line(fd)) == b"CH)O5@SBzW|'XLfK\n"
        assert ffi.string(lib.get_next_line(fd)) == b"Gk:bl}h_6F/TTSf\n"
        assert ffi.string(lib.get_next_line(fd)) == b"oj,2UM=&G|C6?{Cla\n"
        assert ffi.string(lib.get_next_line(fd)) == b"K<RMV%lp'uJ!/T]\n"
        assert ffi.string(lib.get_next_line(fd)) == b"JN0Cl&YWI@p=H!i\n"
        assert ffi.string(lib.get_next_line(fd)) == b"eZY2Y4_4)>u|4d^~\n"
        assert ffi.string(lib.get_next_line(fd)) == b"d*oB$_._w+;pMZ#\n"
        assert ffi.string(lib.get_next_line(fd)) == b"<VY^T&gzWXRmMAD5\n"
        assert ffi.string(lib.get_next_line(fd)) == b"R+^PxI/#pe[8)Z=fQ\n"
        assert ffi.string(lib.get_next_line(fd)) == b'eI-A"#4yluE8wQh@\n'
        assert ffi.string(lib.get_next_line(fd)) == b",~C$QG}P/GuBmT=\n"
        assert ffi.string(lib.get_next_line(fd)) == b"k/Z?:(mEo4P79fA!\n"
        assert ffi.string(lib.get_next_line(fd)) == b"9@hD}NISV'wA3EA'+\n"
        assert ffi.string(lib.get_next_line(fd)) == b"QTk3Wpy^r.Nh@yY\n"
        assert ffi.string(lib.get_next_line(fd)) == b"{(zI@T_wuA27#fRh\n"
        assert ffi.string(lib.get_next_line(fd)) == b"ILQ$)FYw_|uLyX-\n"
        assert ffi.string(lib.get_next_line(fd)) == b"qcA|`+NliDcm)V4L\n"
        assert ffi.string(lib.get_next_line(fd)) == b", yFG~22h?Vd-Wa7j\n"
        assert ffi.string(lib.get_next_line(fd)) == b'MHYE-2fL"G6=L$1Y\n'
        assert ffi.string(lib.get_next_line(fd)) == b"|~AhE[vu)=:MY2!}\n"
        assert ffi.string(lib.get_next_line(fd)) == b'n;[U6.<<e)y"2 T\n'
        assert ffi.string(lib.get_next_line(fd)) == b"[z{s^L]y3`$Hl=jM\n"
        assert ffi.string(lib.get_next_line(fd)) == b"J76w!3iegIHI`$UU1\n"
        assert ffi.string(lib.get_next_line(fd)) == b"xfmQ43j9I9G0AWn \n"
        assert ffi.string(lib.get_next_line(fd)) == b'"Z5FQ{/L6UoH>YP9\n'
        assert ffi.string(lib.get_next_line(fd)) == b'?,"_=ct=K;]-LZNp\n'
        assert ffi.string(lib.get_next_line(fd)) == b"neknaGQz8/A+CM,*a\n"
        assert ffi.string(lib.get_next_line(fd)) == b"m@S=\\Vw0+#t3=11/\n"
        assert ffi.string(lib.get_next_line(fd)) == b"V zolqWM$tflGTL\n"
        assert ffi.string(lib.get_next_line(fd)) == b"J|G>(O|mI+'un/EU0"
        assert lib.get_next_line(fd) == ffi.NULL


def test_mix_31_to_33(lib):
    with open_gnl_file("mix_31_to_33.txt") as fd:
        assert (
            ffi.string(lib.get_next_line(fd)) == b"SR(^tM;5&}\\}ANM8sCY1h8o\\xi6nLXs\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b'l^Nq7"txL: )JL9WB]08Y`<1_3[tcSg\n'
        assert (
            ffi.string(lib.get_next_line(fd)) == b"I]x()}G/^?V=}SQWQZx<06WfOFy)mpKfG\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"sQ^Y2K>f(E49XWe}GuJ''J<QX]p}q6ZM\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"4gY n*F3%@8D[qIevPK*VI]2YMSwmbIP\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"3=4_i@b)C,}<*12bspi[!E$&ei9lY?<~\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"D ak48aT?JG3aWJhTY&V(>3#j*]~iL5i\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"bhrPKZ^%evn5=^i[^m>GT}vV(>$cY(%tJ\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"T:RS`(4D&;wb=C]Lp[kw,Ak75w`8ZU2\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"Kq((cAFLG!KVBhC~'q<-b21D^D`2I@<vk\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"t,E[00J/VU -HP~l'rn0%nIs::pP?w]{\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"d#yS6tU :~Z#P@#8llz1cr@i1sRGbc*bo\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"a]\\& 3j98_tiP*-K{YWGH=o}Jy1*N2.x5\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b'S{T&Ox./mVo*yxxvwOO:&rM<FwA"W6hC;\n'
        )
        assert ffi.string(lib.get_next_line(fd)) == b"55V&Tf[#,4:}Xzst7@zs;s1WVwQj@]E\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b'JM8"H&5zWG56u]:8s>KaUw/r%-#jB9Z0(\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"`uGmZcZxWLQXIl?pzoS5.I9:6v#}RQMf\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"[Pc<mg]7Du{}]VmO4:>_c%csW'omBmo\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"gcHFL=s!=3UsG_rsc(oV,~V\\if;1BF)fe\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"[?BME]OH9/|`0/lVGq3?Y$>VX2`]_j3b+\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"C2$Qjp~[%vaO*]NTS++#Gg_c6f-0|fEkP\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"e@^_PiqO{(TuSEM_jI:6Cyd@|\"^YpH<'N\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"ZnSI[W?g0?* q TDcLF|K(qUFhh&A ^g\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"e[(F9DZN>ko4fgXlT*WlC{.+eXg}+>f+\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"35+GCImV^49Ht'3jJMOR+Ux\\</@!I\"[~\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"3tF0I,A9)ctN>`Q~F}AeN}9U,:,]u[{/F\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"j83dIN\\vi?)PDps 90sX&%P2(*~C>m<\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"Er~tcfZ4{$=OLX[xPCc5QD++ve-*HPu:\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"3wS4jToda*d<FR*R#.r[,<AO&fu!P'h?\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"%^sF5')z%W.G9WWE5P@&VK?))V&^\"{wpW\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b'WChwl)$X+R6=QElimgyG;f.?Jo::*}"!\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"Rw>Y]4>/tU+Ib\\KgRd\"LfdD5:H8o}|J'\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b'zBlOW`u=3Z$Gq"fXP8h3{\\7/7Kb=!@BT=\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b'{62x\\889<~`/A!_qK?"NPExsE yeL0(^\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"OV(:3V64e]u_&|0*,\\vGfo6H+,,LeNA?m\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"Z!BTE9scD**lK:yRx3c*km{1wU*_g/E\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"\\yEAUs)anyir@KfPP'(igU^u7MGAAHH \n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"*smZmIDKRZS\\1dSow3X7{,cESz-`hy6y?\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"**!F1MCuja0q-0>xDXNtTOraw$ gvT2N\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"+6Nqj/gU3irM-?C4gHH=Jty}7gYH[tOh\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b'Ecw^]}"=xcp&cd:|ow_@+6_J QR.y$P+@\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"F!{=.vLd= l41X4svAv,?wN\\qIqG~l7Ox\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b".[.@eljYJNr FEw2I}=hFQXaf!fX {2\n"
        assert ffi.string(lib.get_next_line(fd)) == b'fO9xY-R{]~x,WfK*|+E_c9-GSK]{GK"\n'
        assert (
            ffi.string(lib.get_next_line(fd)) == b"}4Z[ro12*YBGi;<fVw')H><`x*cq~c-A\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"A|J\"(WN*?4hXSN0R,/=0XZ'/9ZhO%{NR\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"CTrG[PVBdwQs,MC$6m;{UA}eVs!h}SD(f\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b'GBA,+HcW_$[D(KSfs"r0B!Z-<K&u`[_go\n'
        )
        assert ffi.string(lib.get_next_line(fd)) == b',bz=n-tLD&=T^]=LnQ$.Ro&Yu" .uA`\n'
        assert ffi.string(lib.get_next_line(fd)) == b'"g9CG%O0F~Y,X(m07|,XKW!DuhVmw\\C.'
        assert lib.get_next_line(fd) == ffi.NULL


def test_mix_41_to_43(lib):
    with open_gnl_file("mix_41_to_43.txt") as fd:
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"$\\\\1bp//x,K5l8X)Dv[JXs]Ryve]#xqoZ/UfgBE/W\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"b:]HFCh]/uvKQ~#MA$6DJ'Zgh$hKNE&B[m}`ROUJn-Q\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"{.pIW,TA%a><]G`/5FP>'ParJS2>l\\}MevvQ6Op9Ms\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"IJoA`g+P;6Wl\\\\7TtXmdKtH~x6qpt~7/>M4kaEm=Z\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"Yxb !]&+lB AZ}A]fUx{PD=2ay)ga*z$ui}E^t+=7\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"yp~qn~8c\\;ngbN<S##8l)2*<$1Oc5A2ET`+ mnfZ$\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"emhHykEad[3.o:A}gVX%jj8o;w6:8H=JuHB!?'RPQE\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"L0sJx/;zXd/OB`zqmShWwcAKcz8C?Z>!b7f\"eUuZQ'\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"e;C2\\qD95-L{W`lJ50hscz4yP`5({G$<hAP26$gm1\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"d#~R2pSBW2C{5..N?QG)hv.\\.[>d.M?uti77>@w<N'*\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'uy"yc2I4$5=$U!t;*=ZL"_sxsbOt";%W"2%]:s|Jmc@\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"6<pj[S&]#sbn`*>bzoh_T]+E569Jf7}BCwcDB|tZE$\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"$!0[o{i<|i 6@9^WN.yQW{fv\\crw^4@SS02B6|*eu/\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"5/8t)wKv+}qV@Q=)\\<u3wmDJaQ<k58qdBLCW,'>mWz5\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'#?acd\\wCe"50_vz(!yJ5dVz}cvE]\\vb{5;LMJ5~0Rm\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"35}sp>UQc;ibyvlt&ck2MB\\)aqvHz@,x@CLA{}TrIm\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"5$Wfjx&n6h|Hukd;H.Lsb{IYe.mr6SN#iPb&Gi&b<\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'2}/Xl.a;UCcE) 8H0W"0)4N i~/Ki\\V&l6<SnF%TS[\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b':){"<{]) n(v,;-rkIJ;JML$Gv,!tcvIVH?=Znq(vmA\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"'zAn#>hz]=x(@5r{xG7sJ$Mr]vU(,O:n#IY1fE%;R\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"B-fS&j.Spx!V]e6yU36)(ML>(b1#@!1*A<>~/ughJ5&\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"O:lS(G/:R2%7=7WK2Z4]u(8k2t[C]z8}ioq= rP^'Ul\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"+jP:fsSV=+)vgz'<139{xLQ1jAK~Fl[V<70BG^0|K\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"(a2li@zwM5JvM1)0ader=Anpq3}#LN#pWmaOT3~*r\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"K=EFy<*:>OKojMYKcnY@e?V)H==H91\\k<(-]M-=Mzn\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"{pc.>a|Cv/>%X[_W2r3<.k<m&jM}<}RCU;yY=~vT5va\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"/=tqLHe@zYl=XSqu!U85%+_`z8wwg11kJw#^Jl?Nl\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b";X1\\!H)>.Y8}&u77Mi6buToyf@{&(l4h}CseFB\\u+\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"{|@>W?tiS[`[,nU#V'y~<lO]3n5\\)yQ6|`h.}+n8|a^\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"WGi-w2CP%4 HSMXb )p1Gd`0b?oc;e3V,^uE% suYR\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"l|GVZ&oepW^'1fr]?gUw(Wgf9!wV74*b,LRj2 R0Q?A\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b' M/Re[KoGT.ZD[U&z1D_6#R"~;^:j:o]6!>hM].Bj\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"j)f7A^mJ.&MzK 3{%/<N0/*VxC}kGg^=N=Zg^F9z.2\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"7:0hs$6nF S4T>,b(i=Ixx:[e^|]<Z1]S]5gj+r~0FT\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"DefqS_&UaxZf$P=T2ymTMeG<mw(/KJ/0`(MX=aH.OT\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"CDbjihp:*[#[CpECHr?L^/nHa-?pZI)s]b3pM~A0ro\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"$^R,Iyn>-V9Pxs>?d*E<z,G8n7FL\\di(M7rgnKm?5\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'8~hgK,R9Kt>vqx7j>;+u+/8"Ngp<1/d@~/n8o,:*m\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"jQBmQ~/$#d6yCQyK|}CLEe'!#^wvW)PaFAcvomzcJ\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'~R`Kk mCtJD>9\\Ty}"n7mg;p :%`K_jtdc("7qcl~_\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"mkvfitv G`7j9@oMZ<CSfhf~J!9j9gV&o31g?+6^5\\\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"k1B!rEHWmOQE=Ud;, tg-c##d(70YDknq$AOD0rn)LR\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"+pjy1<S\\w9e#w+1AC ::B7?+\\`Wz  [^|Ds=ENLwc\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'1]=z4"S_AM8G]GDvDL#w%PY >X4SeG@kib3oQKw?cHS\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'vN%pEZoG`"Vu`r2VRaI*~&[g)-v`6TX6X`19Y,@O7-@\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'8}:F3}Q%Pd-,q4TP`&H@B;!t(^"4S@{s;rX;QusuH1w\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"DMCcY`,7umOJtO~&x!'m+n]t\\mHZ+>W#'azw*tqA7\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"{p4}QP2/!(Vb3{pF#&`<TrD(LURox2l}JS$P#SOsSqe\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"jL#SN~/6ZBuJ^3r:Pm]:iRAQ8fk@ImnF\\Y1E |g{CN#\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"XexA8,hmhp%v)*F<kXVBLtXslz(M#\\lRo `,5,&sb"
        )
        assert lib.get_next_line(fd) == ffi.NULL


def test_newline(lib):
    with open_gnl_file("newline.txt") as fd:
        assert ffi.string(lib.get_next_line(fd)) == b"\n"
        assert lib.get_next_line(fd) == ffi.NULL


def test_single_line_no_trailing_nl(lib):
    with open_gnl_file("single_line_no_trailing_nl.txt") as fd:
        assert ffi.string(lib.get_next_line(fd)) == b"8 r4<O*zrjr)'rg=0NI=7rEu^)dsNdai"
        assert lib.get_next_line(fd) == ffi.NULL


def test_single_line_trailing_nl(lib):
    with open_gnl_file("single_line_trailing_nl.txt") as fd:
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"FU JOIH59 3ONERDFN9URONGJKMDF503IELFD5ONEMDC jer98 5jhny4oy h4y\n"
        )
        assert lib.get_next_line(fd) == ffi.NULL


def test_strict_len_15(lib):
    with open_gnl_file("strict_len_15.txt") as fd:
        assert ffi.string(lib.get_next_line(fd)) == b";E{Qs{Hk<*y/,Aw\n"
        assert ffi.string(lib.get_next_line(fd)) == b'/"HqNJJ.BVq8zm0\n'
        assert ffi.string(lib.get_next_line(fd)) == b"SIt~sbC-d@PFX8o\n"
        assert ffi.string(lib.get_next_line(fd)) == b'C?/t"alv\\}%eO\\w\n'
        assert ffi.string(lib.get_next_line(fd)) == b"Os=i~#1w8,5HVtW\n"
        assert ffi.string(lib.get_next_line(fd)) == b"@S|Q/1_t,MOTTk.\n"
        assert ffi.string(lib.get_next_line(fd)) == b"^Buq%>t/ZdF04UG\n"
        assert ffi.string(lib.get_next_line(fd)) == b"bX)NvJ< Rz$|%X1\n"
        assert ffi.string(lib.get_next_line(fd)) == b"U|A<f]=__w[acX_\n"
        assert ffi.string(lib.get_next_line(fd)) == b"~gs.c9w)stpW@cC"
        assert lib.get_next_line(fd) == ffi.NULL


def test_strict_len_16(lib):
    with open_gnl_file("strict_len_16.txt") as fd:
        assert ffi.string(lib.get_next_line(fd)) == b"OanI`$dVj+*WP*WH\n"
        assert ffi.string(lib.get_next_line(fd)) == b"A9.Yb|Jqeex:~!>o\n"
        assert ffi.string(lib.get_next_line(fd)) == b'n">\\|et3)8]{ueC,\n'
        assert ffi.string(lib.get_next_line(fd)) == b"K9X3#,'P!l^O7O%;\n"
        assert ffi.string(lib.get_next_line(fd)) == b'%48D"lf-O,3pQ&|/\n'
        assert ffi.string(lib.get_next_line(fd)) == b"{vIs9:<&0fqsK;tK\n"
        assert ffi.string(lib.get_next_line(fd)) == b"IW0?G a'xa*~Kr<<\n"
        assert ffi.string(lib.get_next_line(fd)) == b"n2W,F; R&r@<N*/p\n"
        assert ffi.string(lib.get_next_line(fd)) == b"egs$$gp?<Q[V(4!8\n"
        assert ffi.string(lib.get_next_line(fd)) == b"5GFC=:~mf_*gQQ]\\"
        assert lib.get_next_line(fd) == ffi.NULL


def test_strict_len_17(lib):
    with open_gnl_file("strict_len_17.txt") as fd:
        assert ffi.string(lib.get_next_line(fd)) == b".Z|XW`!pAydNn@k;A\n"
        assert ffi.string(lib.get_next_line(fd)) == b";5Cq$i?DEK#hJMVlZ\n"
        assert ffi.string(lib.get_next_line(fd)) == b"@'4@og9t<No\"VAR67\n"
        assert ffi.string(lib.get_next_line(fd)) == b"lYuiF+7;q2JP[/mw.\n"
        assert ffi.string(lib.get_next_line(fd)) == b"4l&*::DL7}Q-tFbs2\n"
        assert ffi.string(lib.get_next_line(fd)) == b"IF37&b9]PONHwUg/?\n"
        assert ffi.string(lib.get_next_line(fd)) == b";)zWPGI9wIp^JsF1H\n"
        assert ffi.string(lib.get_next_line(fd)) == b"2L6AHV?(WS.Ndd}uW\n"
        assert ffi.string(lib.get_next_line(fd)) == b"xu1|3#P4b,gC1'Xs[\n"
        assert ffi.string(lib.get_next_line(fd)) == b"&Ug~?$P)*)%5gL2ln"
        assert lib.get_next_line(fd) == ffi.NULL


def test_strict_len_1(lib):
    with open_gnl_file("strict_len_1.txt") as fd:
        assert ffi.string(lib.get_next_line(fd)) == b"7\n"
        assert ffi.string(lib.get_next_line(fd)) == b"1\n"
        assert ffi.string(lib.get_next_line(fd)) == b"4\n"
        assert ffi.string(lib.get_next_line(fd)) == b"}\n"
        assert ffi.string(lib.get_next_line(fd)) == b"E\n"
        assert ffi.string(lib.get_next_line(fd)) == b"U\n"
        assert ffi.string(lib.get_next_line(fd)) == b"&\n"
        assert ffi.string(lib.get_next_line(fd)) == b"Z\n"
        assert ffi.string(lib.get_next_line(fd)) == b"\\\n"
        assert ffi.string(lib.get_next_line(fd)) == b","
        assert lib.get_next_line(fd) == ffi.NULL


def test_strict_len_31(lib):
    with open_gnl_file("strict_len_31.txt") as fd:
        assert ffi.string(lib.get_next_line(fd)) == b"lR$Q- *Q4>(fj'o.Z^5k&lKW$la~]N>\n"
        assert ffi.string(lib.get_next_line(fd)) == b"<YV+9O`I&wNuH{'Xi6SoNjh7T{2@kD8\n"
        assert ffi.string(lib.get_next_line(fd)) == b"s%bL7p)e{`W.Z]~~[Ge],w= C'P_;'p\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"8'+y:R$T[X{{{i\"QBA2Z;}YE`v C\\Q:\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"{RbT}:l~1zizoB9)uL=)|Jq?^QtEZ;`\n"
        assert ffi.string(lib.get_next_line(fd)) == b'y9ibhQ>8bBJ`4TWW!9t7dpr`3|@S"w2\n'
        assert ffi.string(lib.get_next_line(fd)) == b"egjfO|vNQ$Tv_pi`;sN8O-TgI!~8&zQ\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"\\<l,.)b~3`2b60yhoksGVRFV!ucp{(1\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b'D~Q"5m5,P(gi."E%hrY@426<;pENYw>\n'
        assert ffi.string(lib.get_next_line(fd)) == b'{rODi+"^1QF3~$"DQubZ?Nu|`O;.Ip.'
        assert lib.get_next_line(fd) == ffi.NULL


def test_strict_len_32(lib):
    with open_gnl_file("strict_len_32.txt") as fd:
        assert (
            ffi.string(lib.get_next_line(fd)) == b"e'/terN(\\X`2l><u),x~kmRiwR)XNs|O\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"Y84zbf^F-H/avS%M`Zy_OhM[A!>rNGFj\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"7/;2c/Y4:s;/C*5;ACtT)4Z%d(1z:<+0\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b")|-y;v2Fp_omAz5R/6ntQJr6_aC+)8(/\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"2,=8p*Jx$-3AY<IO(Z$mp~`HS#p>@R^b\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"<0qYuBv!Yf)Cw:gB5rejMw|nAd:VC^`@\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"1'8?\"}Az\\!{NmJ0/wN7;vcXQ59=Yr|#c\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"7m:]1obt^cur^Gr.*N:oVe99$1<hu?3D\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b'gWZ"et_)q7#AAV%zhA$3!iiK3K{K0wWn\n'
        )
        assert ffi.string(lib.get_next_line(fd)) == b"'YmLrpUi\\~-;!Tn!xWb]`hJ@iWyvfo|3"
        assert lib.get_next_line(fd) == ffi.NULL


def test_strict_len_33(lib):
    with open_gnl_file("strict_len_33.txt") as fd:
        assert (
            ffi.string(lib.get_next_line(fd)) == b'cb+d*`*R*T2%B:c"^dXACydcN{Wj{qC>C\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b';`r>:x[@Cr  T`Qz]|`#nsY*$\\o"Ls Z_\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"iYqPi?&'D>2'5=6yStswSE#o?2vU.aA{(\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"@WpX'q|HWW3W ,W :vtyE6g)}}^Ej~5/`\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"<=Do0vv5ZDqj';483ln26c0hOo2W9uMlg\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"=h2sgQM='6|y>7M[?u\"b[`uQW<XcXc3el\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"(<eCR1Y,?/+;E(j*2S,kl@aM9b  @2qPt\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b":#7wRPKTdGn@s:7,V`PIqx{M<FM[7rs-G\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"w`Ed#A<b0 \\7^ljV@MChXqI&$@VqA_?]B\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b'}9a)LwnTv2UgrTJKd@/PEZB0Z"d}7m8 ~'
        assert lib.get_next_line(fd) == ffi.NULL


def test_strict_len_41(lib):
    with open_gnl_file("strict_len_41.txt") as fd:
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"P!e9IU$ZQz'|G7_;]8o`:M)/qXW+pQbl~Q{sd2D[e\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'j*jN./sGc$eN&FBKbR,gM36BnW^r""YkOE_K9r608\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"2n]W`\\m lWGYRxgR$V%e\\0q O?]{[s5:)B]`EFW!H\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"$xbF<-%7IJS4;gHBQlsID*YZXRj1 :B~aEg][[<m1\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"']<(V-XaHP6ei?_N*zmN0;PD?&s-\"tOv~2E.zpyWL\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"VTL9fboG2auTGM+i>+tA[vW7QR.)-E{O=HF>w%VnC\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"~Q>Ryp<pr8GZg)1eA&raR%&qF;@}As{.R17DxQ=7-\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"Tn/J|PfnB3*itU@SrL3T+P=-F!IYU[O5G=:|4IW(%\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'TKrra(tbrQ[Z""XKI[qhow6F}!UF^u/\'CspJGxK,~\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'RA9Ik3:KH/.W7EkZj=fMs|~ZvlgFphtEymJd{ffp"'
        )
        assert lib.get_next_line(fd) == ffi.NULL


def test_strict_len_42(lib):
    with open_gnl_file("strict_len_42.txt") as fd:
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"41nHsH.ZNkL.[pqi\\,:8NjXTV{c1&9AwV++='w.SXd\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'>\\Wh?:j~&gjgR =8kw]gc$P"{/7YSXs3os-[ksab{v\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"MPFoLJ9~5P1|_DVs*vo\\7gWU)bU$y{Xu6`GdfHnCLQ\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"lxB9jhvfMgMw\\qq{S&[;J}mU~a%@*Xxsl-T!APsP|\\\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'mmL^@j5;L1RN[d3/"^;kIq8:(TXxHlG+i/kT1#:j`q\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b":#h&@(SCb}%^G*#@_GO:+U<>HNb>Vl@L~#'!!S`/T6\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'1zixxa}mIaRYD^-L8/MU#"ry:76wT@EdB_J7rdG KI\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"&{UTVz}vuZ7nzr56TZdY-@M:+;436;~_QRp8u/iRDt\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"0YKgtf]kGJCiqnt{)Jlf,iz}Ui6&p~-T@#Ar,t=[C-\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"Zus5k_y|sI:(VLDp8Gjs>o|y1bgzRQ-eH%f'>>.,:`"
        )
        assert lib.get_next_line(fd) == ffi.NULL


def test_strict_len_43(lib):
    with open_gnl_file("strict_len_43.txt") as fd:
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'{$xG|Tn"t?%Q.!iLNLRGb&KQSq3a]r1UsB% 4N,sm+h\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b") UJAUX:Qq&D{0k2U01hiq.V{jLul4318Fyh=I{con!\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"^NQl @?u)ZS2w30D1g@\\S{x>e|<[>lxR5K:KcJ;+UX@\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'<bU-RD@1QIQPcGH_DYN65o?11%GI"7QxVFo]=+]j+,t\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"Tf:N?v4H2qy#Bo*0#DkG4F^oz)s)n5ky5vne+.ET()'\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"`LY`+/|<Ga&uRo3oV9iN))4b0tgD] e|;A/YhwA-Y{n\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'L`I%9l7*Q1smq<E:z,!b>s~"7^HS~"Jjcrwz}c"QQH1\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"7.fQHX{*jJ$Qkq'e#,&4$C+v(b~`!UZP:qd<jn}40\"D\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"$JWLwjSBD|7\\pSLa<$!7K}@I^Mi?KPaz4zUG!}=jC%;\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"*QFZC$Ovu)g_* Z =l7@AoXx&H!d=9qY ):{N$`XbET"
        )
        assert lib.get_next_line(fd) == ffi.NULL


def test_variance_1_to_43_100lines(lib):
    with open_gnl_file("variance_1_to_43_100lines.txt") as fd:
        assert ffi.string(lib.get_next_line(fd)) == b"a|eDDqA%//\n"
        assert ffi.string(lib.get_next_line(fd)) == b"$Pvq=28m23`+\n"
        assert ffi.string(lib.get_next_line(fd)) == b"1VPq93t$;y+SD v(9~(|1\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"Qa_dXcaTPRyqxiSCz~Df^Bq:N,#lKbNUK\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"3\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"cv'kMLD(f73P!e!R;9Uj>i!c]+Bm,;pAZ*,71m*v2q\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'o75`ujlM9av\\0EP0^;KwD-+SBc+z@M|%_DNQU!cB&o"\n'
        )
        assert ffi.string(lib.get_next_line(fd)) == b"-D{ytj]xp AOu,bw;AHvqymI[KwZ\n"
        assert ffi.string(lib.get_next_line(fd)) == b"B<ST\n"
        assert ffi.string(lib.get_next_line(fd)) == b"bjDp8T_MFVe~\\S]T\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"5,l@+>Oancx+2M:;6FUyyY>!pi Y\"ms'S48%M).tTjH\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"F!{2mPxp!A!(C maMk([(TL2.LW}_#1^@VD0$XzL-Y1\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"aF^b(~QUr:#f\n"
        assert ffi.string(lib.get_next_line(fd)) == b"W7TDc'Izt\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b'\\JS~x}yFN39\\}^.&tM/z&^r^55"{\\;\n'
        )
        assert ffi.string(lib.get_next_line(fd)) == b"-ucv=&\n"
        assert ffi.string(lib.get_next_line(fd)) == b'gDUN$mPdkH`d0O0"iaXdzy7}w,5%}(J\n'
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"GHMkqca!72O*NkJw's%0XQHDO.`GlA[7D/F|(N!=\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"]Xtxj#1fUBe+3:~\\yJ{R}>[#+w!$P\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"[[)g1bf3aYr!v%yDaBRr0uhBB1zW{ZY%\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"OYkM=#8>?@yG,#iFclPm~_*3c9k+'_\\n\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"6~R=p^s5Z[{60k%<o7\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"VYq*;dPOaAnR9b-lc~s-J^\\uQ|<3@;<gG@&3}Q1\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"RnX;UQx[9N'o?Xc\\LK/[jTxEv.}ey.D)F\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"@1.ckq.7>LeZrQ-crw%1U|RrPFae\n"
        assert ffi.string(lib.get_next_line(fd)) == b"d5Q\n"
        assert ffi.string(lib.get_next_line(fd)) == b"&T5t.R>.H`!hw6MX3|J`V\n"
        assert ffi.string(lib.get_next_line(fd)) == b".!s|cdc\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"Ev4juOh$f)[C/BFBdM0{+f-u/zV@>7Eq|o^Vu$%]\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"(@bQA~ko@%YjlO\n"
        assert ffi.string(lib.get_next_line(fd)) == b')o:@:j"2mSMN-(nE5T\\Pt=*\n'
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"ML[GCxISiD0FBq-7iNx`U`(uvn~otX^e]J=Le/\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"0s+N>|azE!<3$hw=j\\e\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"+(P\\U`8$5&G-A}kRX.\\{&rw1G=Nx8U%2x#l(\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b'd*tc`gY,"ZN$sX.F%]xe_C*YcD\n'
        assert (
            ffi.string(lib.get_next_line(fd)) == b"nM8]NuzUy^36!JOEI&~]FVm&QvgHLTpBcl\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"5u[-Wo79E\n"
        assert ffi.string(lib.get_next_line(fd)) == b"Wic>3+*[.pVDXj|4yQr_)b\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"}|)5^$x*>%6^dB9zH)Tlyl7Hy+X2X5Bip_\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"V3&\\6c{m\n"
        assert ffi.string(lib.get_next_line(fd)) == b"cTTSlG3dp$sLd=;I'A[\n"
        assert ffi.string(lib.get_next_line(fd)) == b'9"m1?=`0lB[oaZ@w\n'
        assert ffi.string(lib.get_next_line(fd)) == b"/i\n"
        assert ffi.string(lib.get_next_line(fd)) == b'w9"0lW\n'
        assert ffi.string(lib.get_next_line(fd)) == b"w}`84#v4F$MzZ=OH4g?*#a~92,gZ} ;\n"
        assert ffi.string(lib.get_next_line(fd)) == b"96}G{}Zd\\PgcQr_a]<N$5S=M&\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"En:^KH4tnrvxZe`Z+KeRVX|G!C'+`fj7Ll|\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b'.E8XHWguPjrA/mZ6hG4;:A&<%Cjp{##"8U\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'FUmS#+G;`@Y)).Z3?/3\\5 6=#y%pq]hp<"H(B*Q"p\n'
        )
        assert ffi.string(lib.get_next_line(fd)) == b"P^d|=JJsW8Fj@S]F'@ch9Q0Pswe\n"
        assert ffi.string(lib.get_next_line(fd)) == b"LI2~#9A{$^!&N*b}g$ad$hx6us\n"
        assert (
            ffi.string(lib.get_next_line(fd)) == b"|[zDI(o K6]NAx`f,}Iekny',GqionID\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"g~Rev468YV#B^L<vE&p3.<NQ+|W/HYh6p\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"qrfHo_q:'nLS5$e'N]v=Xi&d/Q/'eK\\u\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"O@l`k}fm-'0b*8v9.9ly;8,\\}Hr0'^NJJa;S.61I8\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"=\n"
        assert ffi.string(lib.get_next_line(fd)) == b"}Y!%XRp7 *@\\0)?Uy{z.jZ]_DZK\n"
        assert ffi.string(lib.get_next_line(fd)) == b"(vfMlDD *L$\\)95<w(M[g\n"
        assert ffi.string(lib.get_next_line(fd)) == b"7 =>cHzSyPqTS\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"xgI/f,\\NY'oD\"V U7{OSu9;1fM6:V^(C.zvqbEW\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"+SR&+.Bm{fQ'i\\1ySTAo<\\R|FBe[yE@xou`QN.\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"jE-L\\G9bm';i}cn!oAKLUyOi|$(yDoYa\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"?P:s%iKa%L?iy~hF)Ve1`D(a<:]z,poF !g\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b'O3xJ)/B9Ep?;"veC|}n.b\n'
        assert ffi.string(lib.get_next_line(fd)) == b"X5RV^pJ~`ep%WI\n"
        assert ffi.string(lib.get_next_line(fd)) == b"+@%rI'o<,/6n{7J]dS7Q(?{$h?'?)L\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"-`e!X]_,ZDhn6:4WZ}x\\~OZ}6w|I+;F+<SsN\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"k'j^pK:M;Wk#_CG+\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"z2QPK5PAE(uQcdGi-'d_=5^WEbh/O|?i9a]T\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b";[Z5s\n"
        assert ffi.string(lib.get_next_line(fd)) == b"= _zi%m*+,PW8)4Rsn:x^o0P\n"
        assert ffi.string(lib.get_next_line(fd)) == b"AvRiRhP'(;=C\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b";L0EluU}~9*(C{@|S'G>Tuzj]DAKtTK^E)t7/n@'\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"::\\e<!$AME;Mg'r;t0p_f-\n"
        assert ffi.string(lib.get_next_line(fd)) == b"`p=4JMUVxA\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'>`:Q[Toh&WE`.RsW?=1FR\\/4\\nz5W,.$i"oP\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"[a'sIiKr[(\\J^mphG4[@1dJ}y 0b=Ije00lRz8>Q=\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"krAYFx*'MOHA@4&AP(#M]yzgO&,U.Jk5@N`7q\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"%GZ\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'TZY`yKN_4ZE1>a"S[uVVYEg*sPxz\\jCGC$\n'
        )
        assert ffi.string(lib.get_next_line(fd)) == b';O["r=ubsV>~,3cSC\n'
        assert ffi.string(lib.get_next_line(fd)) == b"NfO\n"
        assert ffi.string(lib.get_next_line(fd)) == b":!?2Q*\n"
        assert ffi.string(lib.get_next_line(fd)) == b"CL`b!C-'KZxlCUqoW\n"
        assert ffi.string(lib.get_next_line(fd)) == b"[\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b" ~J$c4sTF0ro;X%Q^q2Duz{eDTZP!p^~lDMn\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd)) == b"DHDW#)6T+a|HQ^7S(?Nt(pcl}r{Vc&P>b#\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"YIHJ -i#60iF~IOuOe*m9qZ4n5S0z0\n"
        assert ffi.string(lib.get_next_line(fd)) == b'W\\Uh@.f" K}mo9o{9am/>\n'
        assert ffi.string(lib.get_next_line(fd)) == b"F.{Es;?5o2{7DM>N>I\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'{XMCoaWg>b3 o6l$mq>\'U~B"<"$@:UO~3`cyu<",\n'
        )
        assert ffi.string(lib.get_next_line(fd)) == b"Yw,H Rua\\c*K<W=7vC'5j/x)OqP'\n"
        assert ffi.string(lib.get_next_line(fd)) == b" 3Em27>1@~.\n"
        assert ffi.string(lib.get_next_line(fd)) == b'-a0o"&m&r,O#A?F}p>w"\n'
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"-1v8>yI'6zGDe}MU\\z4{rRU%TYU\\L/p_r\n"
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'2RV7"_*yJP.@sBQ#Z?UPgCHv#DilQ ?v=ActGF\n'
        )
        assert ffi.string(lib.get_next_line(fd)) == b"F2h7.miL\n"
        assert (
            ffi.string(lib.get_next_line(fd))
            == b'}O:]_?@ ,i&2Oz4"l6eU0vf9U!P},f&ur-\\"\n'
        )
        assert (
            ffi.string(lib.get_next_line(fd))
            == b"?MYy?l2VM}J;a!X!N54}0a-pp[d[FTr8iA!h7L`TJi0\n"
        )
        assert ffi.string(lib.get_next_line(fd)) == b"5M,^)FIeC]'1:v):-n.GTr0BTGKl"
        assert lib.get_next_line(fd) == ffi.NULL


from random_data_provider import (
    generate_many_lines,
    lines_list_to_str,
)


@pytest.mark.parametrize(
    "line_amount, length_range",
    [
        (10, range(1, 10)),  # Short file, short lines
        (50, range(1, 50)),  # Medium file, varied lines
        (5, range(100, 200)),  # Long lines (tests buffer reallocs)
        (1, range(10, 20)),  # Single line file, no trailing newline
    ],
)
def test_random_data_standard(lib, tmp_path, line_amount, length_range):
    """Test dynamically generated files with 1 newline between lines."""
    # Seed for reproducibility in case of failure
    random.seed(42 + line_amount + length_range.start)

    lines = generate_many_lines(line_amount, length_range)
    content = lines_list_to_str(lines, newlines_in_between=1)

    # Create a temporary file
    f = tmp_path / "random_std.txt"
    f.write_text(content)
    fd = os.open(f, os.O_RDONLY)

    try:
        for i, line in enumerate(lines):
            expected = line.encode("ascii")
            if i < len(lines) - 1:
                expected += b"\n"  # Add newline for all but the last line

            ret = lib.get_next_line(fd)
            assert ret != ffi.NULL, f"GNL returned NULL unexpectedly on line {i}"
            assert ffi.string(ret) == expected

        # Ensure EOF is reached
        assert lib.get_next_line(fd) == ffi.NULL
    finally:
        os.close(fd)


@pytest.mark.parametrize("newlines", [2, 3, 5])
def test_random_data_multiple_newlines(lib, tmp_path, newlines):
    """Test dynamically generated files with multiple newlines between lines."""
    random.seed(99 + newlines)

    lines = generate_many_lines(10, range(5, 30))
    content = lines_list_to_str(lines, newlines_in_between=newlines)

    f = tmp_path / "random_multi_nl.txt"
    f.write_text(content)
    fd = os.open(f, os.O_RDONLY)

    try:
        for i, line in enumerate(lines):
            # The main line content + 1 newline
            expected = (line + "\n").encode("ascii")

            # If it's the last line, it has no trailing newline at all
            if i == len(lines) - 1:
                expected = line.encode("ascii")

            ret = lib.get_next_line(fd)
            assert ret != ffi.NULL
            assert ffi.string(ret) == expected

            # If not the last line, GNL should return the extra newlines as individual lines
            if i < len(lines) - 1:
                for _ in range(newlines - 1):
                    ret_nl = lib.get_next_line(fd)
                    assert ret_nl != ffi.NULL
                    assert ffi.string(ret_nl) == b"\n"

        assert lib.get_next_line(fd) == ffi.NULL
    finally:
        os.close(fd)


def test_random_huge_stress(lib, tmp_path):
    """Stress test with a large amount of random data."""
    random.seed(1337)

    # 500 lines, lengths varying from 1 to 1000 characters
    lines = generate_many_lines(500, range(1, 1000))
    content = lines_list_to_str(lines, newlines_in_between=1)

    f = tmp_path / "stress_test.txt"
    f.write_text(content)
    fd = os.open(f, os.O_RDONLY)

    try:
        for i, line in enumerate(lines):
            expected = line.encode("ascii")
            if i < len(lines) - 1:
                expected += b"\n"

            ret = lib.get_next_line(fd)
            assert ret != ffi.NULL, f"Crash or NULL on line {i} (len {len(line)})"
            assert ffi.string(ret) == expected

        assert lib.get_next_line(fd) == ffi.NULL
    finally:
        os.close(fd)
