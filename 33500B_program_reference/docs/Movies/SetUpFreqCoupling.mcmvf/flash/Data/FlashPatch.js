var objectNodes = document.getElementsByTagName( "object" );

for ( var i = 0; i < objectNodes.length; i++)
{
	objectNodes[i].outerHTML = objectNodes[i].outerHTML;
}
