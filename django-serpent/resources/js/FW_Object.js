/*
 * This file contains functions to generate OBJECT, EMBED, and APPLET tags.
 * Adapted from AC_QuickTime.js 
 */

var gTagAttrs = null;

function _FWAddAttribute(prefix, slotName, tagName)
{
	var		value;

	value = gTagAttrs[prefix + slotName];
	if ( null == value )
		value = gTagAttrs[slotName];

	if ( null != value )
	{
		if ( 0 == slotName.indexOf(prefix) && (null == tagName) )
			tagName = slotName.substring(prefix.length); 
		if ( null == tagName ) 
			tagName = slotName;
		return tagName + '="' + value + '" ';
	}
	else
		return "";
}

function _FWAddObjectAttr(slotName, tagName)
{
	if ( 0 == slotName.indexOf("emb#") )
		return "";

	if ( 0 == slotName.indexOf("obj#") && (null == tagName) )
		tagName = slotName.substring(4); 

	return _FWAddAttribute("obj#", slotName, tagName);
}

function _FWAddEmbedAttr(slotName, tagName)
{
	if ( 0 == slotName.indexOf("obj#") )
		return "";

	if ( 0 == slotName.indexOf("emb#") && (null == tagName) )
		tagName = slotName.substring(4); 

	return _FWAddAttribute("emb#", slotName, tagName);
}

function _FWAddAppletAttr(slotName, tagName)
{
	if ( 0 == slotName.indexOf("obj#") )
		return "";

	if ( 0 == slotName.indexOf("app#") && (null == tagName) )
		tagName = slotName.substring(4); 

	return _FWAddAttribute("app#", slotName, tagName);
}

function _FWAddObjectParam(slotName, generateXHTML)
{
	var		paramValue;
	var		paramStr = "";
	var		endTagChar = (generateXHTML) ? ' />' : '>';

	if ( -1 == slotName.indexOf("emb#") )
	{
		paramValue = gTagAttrs["obj#" + slotName];
		if ( null == paramValue )
			paramValue = gTagAttrs[slotName];

		if ( 0 == slotName.indexOf("obj#") )
			slotName = slotName.substring(4); 
	
		if ( null != paramValue )
			paramStr = '  <param name="' + slotName + '" value="' + paramValue + '"' + endTagChar + '\n';
	}

	return paramStr;
}

function _FWDeleteTagAttrs()
{
	for ( var ndx = 0; ndx < arguments.length; ndx++ )
	{
		var attrName = arguments[ndx];
		delete gTagAttrs[attrName];
		delete gTagAttrs["emb#" + attrName];
		delete gTagAttrs["obj#" + attrName];
	}
}

function _FWGenerate(args)
{
	if ( args.length < 8 || (0 != (args.length % 2)) )
	{
		return "";
	}
	
	gTagAttrs = new Array();
	gTagAttrs["src"] = args[0];
	gTagAttrs["width"] = args[1];
	gTagAttrs["height"] = args[2];
	
	var generateXHTML = ("true" == args[4]);
	var contentType = args[5];
	var altText = args[6];
	
	if (altText != "")
		altText = altText + '\n';
	
	if ("quicktime" == contentType)
	{
		gTagAttrs["classid"] = "clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B";
		gTagAttrs["pluginspage"] = "http://www.apple.com/quicktime/download/";

		var activexVers = args[3]
		if ( (null == activexVers) || ("" == activexVers) )
			activexVers = "6,0,2,0";
		gTagAttrs["codebase"] = "http://www.apple.com/qtactivex/qtplugin.cab#version=" + activexVers;
	}
	else if ("flash" == contentType)
	{
		gTagAttrs["classid"] = "clsid:D27CDB6E-AE6D-11cf-96B8-444553540000";
		gTagAttrs["pluginspage"] = "http://www.macromedia.com/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash";

		var activexVers = args[3]
		if ( (null == activexVers) || ("" == activexVers) )
			activexVers = "8,0,24,0";
		gTagAttrs["codebase"] = "http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=" + activexVers;
	}

	var	attrName,
		attrValue;

	for ( var ndx = 8; ndx < args.length; ndx += 2)
	{
		attrName = args[ndx].toLowerCase();
		attrValue = args[ndx + 1];

		if ( "name" == attrName || "id" == attrName )
			gTagAttrs["name"] = attrValue;

		else 
			gTagAttrs[attrName] = attrValue;
	}

	var objTag =  '<object '
					+ _FWAddObjectAttr("classid")
					+ _FWAddObjectAttr("width")
					+ _FWAddObjectAttr("height")
					+ _FWAddObjectAttr("codebase")
					+ _FWAddObjectAttr("name", "id")
					+ _FWAddObjectAttr("tabindex")
					+ _FWAddObjectAttr("hspace")
					+ _FWAddObjectAttr("vspace")
					+ _FWAddObjectAttr("border")
					+ _FWAddObjectAttr("align")
					+ _FWAddObjectAttr("class")
					+ _FWAddObjectAttr("title")
					+ _FWAddObjectAttr("accesskey")
					+ _FWAddObjectAttr("noexternaldata")
					+ _FWAddObjectAttr("style")
					+ '>\n'
					+ _FWAddObjectParam("src", generateXHTML);
	var embedTag = '  <embed '
					+ _FWAddEmbedAttr("src")
					+ _FWAddEmbedAttr("width")
					+ _FWAddEmbedAttr("height")
					+ _FWAddEmbedAttr("pluginspage")
					+ _FWAddEmbedAttr("name")
					+ _FWAddEmbedAttr("align")
					+ _FWAddEmbedAttr("tabindex");

	_FWDeleteTagAttrs("src","width","height","pluginspage","classid","codebase","name","tabindex",
					"hspace","vspace","border","align","noexternaldata","class","title","accesskey","style");

	for ( var attrName in gTagAttrs )
	{
		attrValue = gTagAttrs[attrName];
		if ( null != attrValue )
		{
			embedTag += _FWAddEmbedAttr(attrName);
			objTag += _FWAddObjectParam(attrName, generateXHTML);
		}
	} 

	return objTag + embedTag + '> \n' + '</ob' + 'ject' + '>';
}

function _FWGenerateApplet(args)
{
	if ( args.length < 6 || (0 != (args.length % 2)) )
	{
		return "";
	}

	gTagAttrs = new Array();
	gTagAttrs["code"] = args[0];
	gTagAttrs["width"] = args[1];
	gTagAttrs["height"] = args[2];
	
	var generateXHTML = ("true" == args[4]);
	var altText = args[5];
	
	if (altText != "")
		altText = altText + '\n';
	
	var	attrName,
		attrValue;

	for ( var ndx = 6; ndx < args.length; ndx += 2)
	{
		attrName = args[ndx].toLowerCase();
		attrValue = args[ndx + 1];

		if ( "name" == attrName || "id" == attrName )
			gTagAttrs["name"] = attrValue;

		else 
			gTagAttrs[attrName] = attrValue;
	}
	
	var appletTag = '  <applet '
					+ _FWAddAppletAttr("code")
					+ _FWAddAppletAttr("width")
					+ _FWAddAppletAttr("height")
					+ _FWAddAppletAttr("codebase")
					+ _FWAddAppletAttr("name")
					+ _FWAddAppletAttr("tabindex")
					+ _FWAddAppletAttr("hspace")
					+ _FWAddAppletAttr("vspace")
					+ _FWAddAppletAttr("border")
					+ _FWAddAppletAttr("align")
					+ _FWAddAppletAttr("alt")
					+ _FWAddAppletAttr("class")
					+ _FWAddAppletAttr("title")
					+ _FWAddAppletAttr("style");

	_FWDeleteTagAttrs("code","width","height","codebase","name","tabindex",
					"hspace","vspace","border","align","alt","class","title","style");

	for ( var attrName in gTagAttrs )
	{
		attrValue = gTagAttrs[attrName];
		if ( null != attrValue )
		{
			appletTag += _FWAddAppletAttr(attrName);
		}
	} 
	
	return appletTag + '> </app' + 'let' + '>';
}

function FW_WriteObject()
{
	document.writeln(_FWGenerate(arguments));
}

function FW_WriteApplet()
{
	document.writeln(_FWGenerateApplet(arguments));
}

