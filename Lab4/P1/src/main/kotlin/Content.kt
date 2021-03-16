class content(private var author: String, private var text:String, private var name:String, private var publisher:String )
{
    fun get_author():String
    {
        println("Numele autorului este:")
        return  author;
    }
    fun set_author( aut:String)
    {
        this.author = aut;
    }
    fun get_text():String
    {
        println("Textul este:");
        return text;
    }
    fun set_text(txt:String)
    {
        this.text = txt;
    }
    fun get_name():String
    {
        println("Numele este:");
        return name;
    }
    fun set_name(names:String)
    {
        this.name = names;
    }
    fun get_pub():String{
        println("Publicatia: ");
        return publisher;
    }
    fun set_pub(pubs:String)
    {
        this.publisher = pubs;
    }
}