class book(private var content:content)
{
    override fun toString(): String {
        return "${content.get_author()}.${content.get_name()}.${content.get_pub()}.${content.get_text()}"

    }
    fun get_n():String{
        return content.get_name();
    }
    fun get_a():String{
        return content.get_author();
    }
    fun get_p():String{
        return content.get_pub();
    }
    fun get_content():String
    {
        return toString();
    }
    fun has_author(aut :String):Boolean
    {
        if(content.get_author()==aut) {
            return true;

        }
        else
            return false;
    }
    fun has_Titile(tit :String):Boolean
    {
        if(content.get_pub() == tit)
        {
            return true;
        }
        else
            return false;
    }
    fun has_pub(pub :String):Boolean
    {
        if(content.get_pub() == pub)
        {
            return true;
        }
        else
            return false
    }
}