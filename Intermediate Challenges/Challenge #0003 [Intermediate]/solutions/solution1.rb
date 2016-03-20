# Author: Lim Yao Jie
# Description: Subsitution Cipher + Transposition Cipher together.

module Main

  def self.init
    STDOUT.sync = true
    
    puts "Type in a number to begin."
    puts "1: Encrypt Message"
    puts "2: Decrypt Message"
    choice = gets.chomp

    c = choice.to_i
    
    if c == 1
    
      puts "Type your message to be encrypted:"
      message = gets.chomp
      puts "Processing.."
      t_cipher = ColumnarTranspositionCipher.new
      encrypted_message = t_cipher.get_encrypted_message(message)
      puts "Your encrypted message is: \n#{encrypted_message}"
    elsif c == 2
    
      puts "Type your message to be decrypted:"
      message = gets.chomp
      puts "Processing.."
      t_cipher = ColumnarTranspositionCipher.new
      decrypted_message = t_cipher.get_decrypted_message(message)
      puts "Your decrypted_message is: \n#{decrypted_message}"
    else
      puts "Invalid choice!"
      self.init
    end
  end
end

class SubsitutionCipher
end

class ColumnarTranspositionCipher

  def initialize(*args)

    @key = "rickastley"
    @original_key = @key.codepoints
    @sorted_key = @original_key.sort

    @transpose = []
    @transpose_indexes = []

    # get transposed keys based on sorted index of original keys
    @original_key.each {|k| @transpose << @sorted_key.find_index(k) } 

    # return encrypted message based on transposed index
    (0..@transpose.length-1).each {|i| @transpose_indexes << @transpose.find_index(i) }
  end


  def get_encrypted_message(message)
    len = message.length
    padding_size = @original_key.length % len

    puts "Original: #{@original_key}"
    puts "Sorted: #{@sorted_key}"
    puts "Transposed: #{@transpose}"
    puts "Tranposed Indexes: #{@transpose_indexes}"

    message_arr = message.split("").each_slice(@original_key.length).to_a
    puts "Message Array: #{message_arr}"

    encrypted_message = ""

    message_arr.each do |arr|
      # row
      row_chunk = []
      arr.each_with_index do |char, index|
        # character
        row_chunk[@transpose_indexes[index]] = char
      end
      puts "Row Chunk: #{row_chunk}"
      encrypted_message << row_chunk.join("")
    end

    return encrypted_message
  end

  def get_decrypted_message(message)
    message_arr = message.split("").each_slice(@original_key.length).to_a
    puts "Message Array: #{message_arr}"

    decrypted_message = ""
    message_arr.each do |arr|
      # row
      row_chunk = []
      arr.each_with_index do |char, index|
        # character
        row_chunk[@transpose[index]] = char
      end
      puts "Row Chunk: #{row_chunk}"
      decrypted_message << row_chunk.join("")
    end
    return decrypted_message
  end

end

Main.init