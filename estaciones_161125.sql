--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: estaciones; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE estaciones (
    numeroserie character varying(50) DEFAULT 'null'::character varying,
    numerocartel character varying(10),
    ip character varying(50),
    linea character varying(1),
    estacion character varying(30),
    datetime character varying(30) DEFAULT 'null'::character varying,
    ping boolean DEFAULT false
);


ALTER TABLE estaciones OWNER TO postgres;

--
-- Data for Name: estaciones; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY estaciones (numeroserie, numerocartel, ip, linea, estacion, datetime, ping) FROM stdin;
null	21503	172.30.49.164	b	los incas	16-11-22_15:45:26	f
null	51801	172.30.108.121	E	plaza de los virreyes	16-11-22_15:45:27	f
null	51803	172.30.108.123	E	plaza de los virreyes	16-11-22_15:45:28	f
null	21323	172.30.49.157	b	federico lacroze	16-11-22_15:45:29	f
null	90001	172.21.8.17	E	bonifacio	16-11-22_15:45:30	f
null	70301	172.26.155.100	H	hospitales	16-11-22_15:45:31	f
null	70402	172.26.155.102	H	parque de los patricios	16-11-22_15:45:32	f
null	70502	172.26.155.104	H	caseros	16-11-22_15:45:33	f
null	70501	172.26.155.103	H	caseros	16-11-22_15:45:34	f
null	70601	172.26.155.105	H	inclan	16-11-22_15:45:35	f
null	70611	172.26.155.106	H	inclan	16-11-22_15:45:36	f
null	70701	172.26.155.107	H	humberto primo	16-11-22_15:45:37	f
null	70711	172.26.155.108	H	humberto primo	16-11-22_15:45:38	f
null	70801	172.26.155.109	H	venezuela	16-11-22_15:45:39	f
null	70901	172.26.155.110	H	once	16-11-22_15:45:40	f
null	71001	172.26.155.112	H	corrientes	16-11-22_15:45:41	f
null	71101	172.26.155.113	H	cordoba	16-11-22_15:45:42	f
null	71102	172.26.155.114	H	cordoba	16-11-22_15:45:43	f
null	71103	172.26.155.115	H	cordoba	16-11-22_15:45:44	f
null	71104	172.26.155.116	H	cordoba	16-11-22_15:45:45	f
null	71212	172.26.155.119	H	santa fe	16-11-22_15:45:47	f
null	71213	172.26.155.120	H	santa fe	16-11-22_15:45:48	f
null	71202	172.26.155.122	H	santa fe	16-11-22_15:45:49	f
null	71203	172.26.155.123	H	santa fe	16-11-22_15:45:50	f
null	71221	172.26.155.124	H	santa fe	16-11-22_15:45:51	f
null	71222	172.26.155.125	H	santa fe	16-11-22_15:45:52	f
null	71302	172.26.155.127	H	las heras	16-11-22_15:45:53	f
null	21702	172.30.49.169	b	juan manuel de rosas	16-11-22_15:45:54	f
null	50401	172.30.108.100	E	bolivar	16-11-22_15:45:55	f
null	21301	172.30.49.154	b	federico lacroze	16-11-22_15:45:56	f
null	71303	172.26.155.128	H	las heras	16-11-22_15:45:57	f
null	71304	172.26.155.129	H	las heras	16-11-22_15:45:58	f
null	20201	172.30.49.105	b	florida	16-11-22_15:45:59	f
null	21322	172.30.49.156	b	federico lacroze	16-11-22_15:46:00	f
null	21013	172.30.49.142	b	angel gallardo	16-11-22_15:46:01	f
null	51402	172.30.108.117	E	jose maria moreno	16-11-22_15:46:02	f
null	20101	172.30.49.100	b	leandro n alem	16-11-22_15:46:03	f
null	20102	172.30.49.101	b	leandro n alem	16-11-22_15:46:04	f
null	20103	172.30.49.102	b	leandro n alem	16-11-22_15:46:05	f
null	20104	172.30.49.103	b	leandro n alem	16-11-22_15:46:06	f
null	20211	172.30.49.106	b	florida	16-11-22_15:46:07	f
null	20212	172.30.49.107	b	florida	16-11-22_15:46:08	f
null	20213	172.30.49.108	b	florida	16-11-22_15:46:10	f
null	20214	172.30.49.109	b	florida	16-11-22_15:46:11	f
null	20301	172.30.49.110	b	carlos pelegrini	16-11-22_15:46:12	f
null	20303	172.30.49.112	b	carlos pelegrini	16-11-22_15:46:13	f
null	20311	172.30.49.114	b	carlos pelegrini	16-11-22_15:46:14	f
null	20401	172.30.49.115	b	uruguay	16-11-22_15:46:15	f
null	20402	172.30.49.116	b	uruguay	16-11-22_15:46:16	f
null	20403	172.30.49.117	b	uruguay	16-11-22_15:46:17	f
null	20501	172.30.49.119	b	callao	16-11-22_15:46:18	f
null	20502	172.30.49.120	b	callao	16-11-22_15:46:19	f
null	20503	172.30.49.121	b	callao	16-11-22_15:46:20	f
null	20601	172.30.49.123	b	pasteur	16-11-22_15:46:21	f
null	20603	172.30.49.125	b	pasteur	16-11-22_15:46:22	f
null	20701	172.30.49.126	b	pueyrredon	16-11-22_15:46:23	f
null	20702	172.30.49.127	b	pueyrredon	16-11-22_15:46:24	f
null	20704	172.30.49.129	b	pueyrredon	16-11-22_15:46:25	f
null	20802	172.30.49.131	b	carlos gardel	16-11-22_15:46:26	f
null	20803	172.30.49.132	b	carlos gardel	16-11-22_15:46:27	f
null	20804	172.30.49.133	b	carlos gardel	16-11-22_15:46:28	f
null	20912	172.30.49.136	b	medrano	16-11-22_15:46:29	f
null	20913	172.30.49.137	b	medrano	16-11-22_15:46:30	f
null	20914	172.30.49.138	b	medrano	16-11-22_15:46:31	f
null	21001	172.30.49.139	b	angel gallardo	16-11-22_15:46:32	f
null	21012	172.30.49.141	b	angel gallardo	16-11-22_15:46:33	f
null	21101	172.30.49.144	b	malabia	16-11-22_15:46:34	f
null	21111	172.30.49.145	b	malabia	16-11-22_15:46:35	f
null	21112	172.30.49.146	b	malabia	16-11-22_15:46:36	f
null	21113	172.30.49.147	b	malabia	16-11-22_15:46:37	f
null	21201	172.30.49.149	b	dorrego	16-11-22_15:46:39	f
null	21211	172.30.49.150	b	dorrego	16-11-22_15:46:40	f
null	21212	172.30.49.151	b	dorrego	16-11-22_15:46:41	f
null	21324	172.30.49.158	b	federico lacroze	16-11-22_15:46:42	f
null	21331	172.30.49.159	b	federico lacroze	16-11-22_15:46:43	f
null	21332	172.30.49.160	b	federico lacroze	16-11-22_15:46:44	f
null	21501	172.30.49.162	b	los incas	16-11-22_15:46:45	f
null	21502	172.30.49.163	b	los incas	16-11-22_15:46:46	f
null	51804	172.30.108.124	E	plaza de los virreyes	16-11-22_15:46:47	f
null	21701	172.30.49.168	b	juan manuel de rosas	16-11-22_15:46:48	f
null	50402	172.30.108.101	E	bolivar	16-11-22_15:46:49	f
null	20302	172.30.49.111	b	carlos pelegrini	16-11-22_15:46:50	f
null	20404	172.30.49.118	b	uruguay	16-11-22_15:46:51	f
null	40902	172.30.88.134	d	scalabrini ortiz	16-11-22_15:46:52	f
null	21714	172.30.49.173	b	juan manuel de rosas	16-11-22_15:46:53	f
null	40102	172.30.88.101	d	catedral	16-11-22_15:46:54	f
null	40111	172.30.88.102	d	catedral	16-11-22_15:46:55	f
null	40112	172.30.88.103	d	catedral	16-11-22_15:46:56	f
null	40114	172.30.88.105	d	catedral	16-11-22_15:46:57	f
null	40201	172.30.88.106	d	9 de julio	16-11-22_15:46:58	f
null	40211	172.30.88.108	d	9 de julio	16-11-22_15:46:59	f
null	40221	172.30.88.109	d	9 de julio	16-11-22_15:47:00	f
null	40312	172.30.88.111	d	tribunales	16-11-22_15:47:01	f
null	40313	172.30.88.112	d	tribunales	16-11-22_15:47:02	f
null	40401	172.30.88.113	d	callao	16-11-22_15:47:03	f
null	40412	172.30.88.115	d	callao	16-11-22_15:47:04	f
null	40501	172.30.88.117	d	facultad de medicina	16-11-22_15:47:06	f
null	40503	172.30.88.119	d	facultad de medicina	16-11-22_15:47:07	f
null	40504	172.30.88.120	d	facultad de medicina	16-11-22_15:47:08	f
null	40601	172.30.88.121	d	pueyrredon	16-11-22_15:47:09	f
null	40603	172.30.88.123	d	pueyrredon	16-11-22_15:47:10	f
null	40701	172.30.88.124	d	aguero	16-11-22_15:47:11	f
null	40702	172.30.88.125	d	aguero	16-11-22_15:47:12	f
null	40801	172.30.88.128	d	bulnes	16-11-22_15:47:13	f
null	40811	172.30.88.129	d	bulnes	16-11-22_15:47:14	f
null	40812	172.30.88.130	d	bulnes	16-11-22_15:47:15	f
null	40901	172.30.88.133	d	scalabrini ortiz	16-11-22_15:47:16	f
null	40911	172.30.88.135	d	scalabrini ortiz	16-11-22_15:47:17	f
null	40912	172.30.88.136	d	scalabrini ortiz	16-11-22_15:47:18	f
null	41001	172.30.88.137	d	plaza italia	16-11-22_15:47:19	f
null	41002	172.30.88.138	d	plaza italia	16-11-22_15:47:20	f
null	41013	172.30.88.141	d	plaza italia	16-11-22_15:47:21	f
null	41014	172.30.88.142	d	plaza italia	16-11-22_15:47:22	f
null	41101	172.30.88.143	d	palermo	16-11-22_15:47:23	f
null	40101	172.30.88.100	d	catedral	16-11-22_15:47:24	f
null	50411	172.30.108.102	E	bolivar	16-11-22_15:47:25	f
null	50601	172.30.108.104	E	independencia	16-11-22_15:47:26	f
null	50602	172.30.108.105	E	independencia	16-11-22_15:47:27	f
null	50701	172.30.108.106	E	san jose	16-11-22_15:47:28	f
null	50801	172.30.108.107	E	entre rios	16-11-22_15:47:29	f
null	50901	172.30.108.109	E	pichincha	16-11-22_15:47:30	f
null	51001	172.30.108.110	E	jujuy	16-11-22_15:47:32	f
null	51101	172.30.108.111	E	urquiza	16-11-22_15:47:33	f
null	51201	172.30.108.112	E	boedo	16-11-22_15:47:34	f
null	5120	172.30.108.113	E	boedo	16-11-22_15:47:35	f
null	51302	172.30.108.115	E	La plata	16-11-22_15:47:36	f
null	51401	172.30.108.116	E	jose maria moreno	16-11-22_15:47:37	f
null	51501	172.30.108.118	E	emilio mitre	16-11-22_15:47:38	f
null	41102	172.30.88.144	d	palermo	16-11-22_15:47:39	f
null	41104	172.30.88.146	d	palermo	16-11-22_15:47:40	f
null	41202	172.30.88.148	d	ministro carranza	16-11-22_15:47:41	f
null	41203	172.30.88.149	d	ministro carranza	16-11-22_15:47:42	f
null	41301	172.30.88.150	d	olleros	16-11-22_15:47:43	f
null	41303	172.30.88.152	d	olleros	16-11-22_15:47:44	f
null	41304	172.30.88.153	d	olleros	16-11-22_15:47:45	f
null	41401	172.30.88.154	d	jose hernandez	16-11-22_15:47:46	f
null	41404	172.30.88.157	d	jose hernandez	16-11-22_15:47:47	f
null	41501	172.30.88.158	d	juramento	16-11-22_15:47:48	f
null	41502	172.30.88.159	d	juramento	16-11-22_15:47:49	f
null	41504	172.30.88.161	d	juramento	16-11-22_15:47:50	f
null	41601	172.30.88.162	d	congreso de tucuman	16-11-22_15:47:51	f
null	41604	172.30.88.165	d	congreso de tucuman	16-11-22_15:47:52	f
null	41605	172.30.88.166	d	congreso de tucuman	16-11-22_15:47:53	f
null	41606	172.30.88.167	d	congreso de tucuman	16-11-22_15:47:54	f
null	41607	172.30.88.168	d	congreso de tucuman	16-11-22_15:47:55	f
null	20602	172.30.49.124	b	pasteur	16-11-22_15:47:56	f
null	20911	172.30.49.135	b	medrano	16-11-22_15:47:57	f
null	21011	172.30.49.140	b	angel gallardo	16-11-22_15:47:58	f
null	21114	172.30.49.148	b	malabia	16-11-22_15:48:00	f
null	21214	172.30.49.153	b	dorrego	16-11-22_15:48:01	f
null	21401	172.30.49.161	b	tronador	16-11-22_15:48:02	f
null	21602	172.30.49.167	b	echeverria	16-11-22_15:48:03	f
null	21713	172.30.49.172	b	juan manuel de rosas	16-11-22_15:48:04	f
null	40113	172.30.88.104	d	catedral	16-11-22_15:48:05	f
null	40311	172.30.88.110	d	tribunales	16-11-22_15:48:06	f
null	40421	172.30.88.116	d	callao	16-11-22_15:48:07	f
null	40602	172.30.88.122	d	pueyrredon	16-11-22_15:48:08	f
null	21712	172.30.49.171	b	juan manuel de rosas	16-11-22_15:48:22	f
null	41103	172.30.88.145	d	palermo	16-11-22_15:48:23	f
null	40202	172.30.88.107	d	9 de julio	16-11-22_15:48:39	f
null	40502	172.30.88.118	d	facultad de medicina	16-11-22_15:48:24	f
null	20703	172.30.49.128	b	pueyrredon	16-11-22_15:48:25	f
null	51601	172.30.108.119	E	medalla milagrosa	16-11-22_15:48:40	f
null	40814	172.30.88.132	d	bulnes	16-11-22_15:48:27	f
null	41402	172.30.88.155	d	jose hernandez	16-11-22_15:48:28	f
null	41201	172.30.88.147	d	ministro carranza	16-11-22_15:48:41	f
null	40703	172.30.88.126	d	aguero	16-11-22_15:48:29	f
null	70902	172.26.155.111	H	once	16-11-22_15:48:30	f
null	41503	172.30.88.160	d	juramento	16-11-22_15:48:42	f
null	51301	172.30.108.114	E	La plata	16-11-22_15:48:31	f
null	40704	172.30.88.127	d	aguero	16-11-22_15:48:09	f
null	41603	172.30.88.164	d	congreso de tucuman	16-11-22_15:48:43	f
null	70401	172.26.155.101	H	parque de los patricios	16-11-22_15:48:44	f
null	51701	172.30.108.120	E	varela	16-11-22_15:48:10	f
null	41302	172.30.88.151	d	olleros	16-11-22_15:48:32	f
null	21711	172.30.49.170	b	juan manuel de rosas	16-11-22_15:48:45	f
null	21504	172.30.49.165	b	los incas	16-11-22_15:48:11	f
null	41403	172.30.88.156	d	jose hernandez	16-11-22_15:48:46	f
null	40411	172.30.88.114	d	callao	16-11-22_15:48:47	f
null	21014	172.30.49.143	b	angel gallardo	16-11-22_15:48:12	f
null	40813	172.30.88.131	d	bulnes	16-11-22_15:48:48	f
null	20504	172.30.49.122	b	callao	16-11-22_15:48:33	f
null	50501	172.30.108.103	E	belgrano	16-11-22_15:48:13	f
null	21213	172.30.49.152	b	dorrego	16-11-22_15:48:49	f
null	21601	172.30.49.166	b	echeverria	16-11-22_15:48:50	f
null	71211	172.26.155.118	H	santa fe	16-11-22_15:48:51	f
null	41011	172.30.88.139	d	plaza italia	16-11-22_15:48:14	f
null	41012	172.30.88.140	d	plaza italia	16-11-22_15:48:34	f
null	20901	172.30.49.134	b	medrano	16-11-22_15:48:15	f
null	50802	172.30.108.108	E	entre rios	16-11-22_15:48:16	f
null	20105	172.30.49.104	b	leandro n alem	16-11-22_15:48:35	f
null	71301	172.26.155.126	H	las heras	16-11-22_15:48:17	f
null	20304	172.30.49.113	b	carlos pelegrini	16-11-22_15:48:18	f
null	51802	172.30.108.122	E	plaza de los virreyes	16-11-22_15:48:36	f
null	21321	172.30.49.155	b	federico lacroze	16-11-22_15:48:19	f
null	20801	172.30.49.130	b	carlos gardel	16-11-22_15:48:20	f
null	41608	172.30.88.169	d	congreso de tucuman	16-11-22_15:48:37	f
null	71201	172.26.155.121	H	santa fe	16-11-22_15:48:21	f
null	41602	172.30.88.163	d	congreso de tucuman	16-11-22_15:48:38	f
\.


--
-- PostgreSQL database dump complete
--

